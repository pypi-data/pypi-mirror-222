import typing as t

from pymongo.results import DeleteResult, InsertOneResult, UpdateResult

from superduperdb.container.component import Component
from superduperdb.db.base.metadata import MetaDataStore


class MongoMetaDataStore(MetaDataStore):
    def __init__(
        self,
        conn: t.Any,
        name: t.Optional[str] = None,
    ) -> None:
        self.name = name
        db = conn[name]
        self.meta_collection = db['_meta']
        self.object_collection = db['_objects']
        self.job_collection = db['_jobs']
        self.parent_child_mappings = db['_parent_child_mappings']

    def create_parent_child(self, parent: str, child: str) -> None:
        self.parent_child_mappings.insert_one(
            {
                'parent': parent,
                'child': child,
            }
        )

    def create_component(self, info: t.Dict) -> InsertOneResult:
        if 'hidden' not in info:
            info['hidden'] = False
        return self.object_collection.insert_one(info)

    def create_job(self, info: t.Dict) -> InsertOneResult:
        return self.job_collection.insert_one(info)

    def get_parent_child_relations(self):
        c = self.parent_child_mappings.find()
        return [(r['parent'], r['child']) for r in c]

    def get_component_version_children(self, unique_id: str):
        return self.parent_child_mappings.distinct('child', {'parent': unique_id})

    def get_job(self, identifier: str):
        return self.job_collection.find_one({'identifier': identifier})

    def get_metadata(self, key: str):
        return self.meta_collection.find_one({'key': key})['value']

    def get_latest_version(
        self, type_id: str, identifier: str, allow_hidden: bool = False
    ) -> int:
        try:
            if allow_hidden:
                return sorted(
                    self.object_collection.distinct(
                        'version', {'identifier': identifier, 'type_id': type_id}
                    )
                )[-1]
            else:
                return sorted(
                    self.object_collection.distinct(
                        'version',
                        {
                            '$or': [
                                {
                                    'identifier': identifier,
                                    'type_id': type_id,
                                    'hidden': False,
                                },
                                {
                                    'identifier': identifier,
                                    'type_id': type_id,
                                    'hidden': {'$exists': 0},
                                },
                            ]
                        },
                    )
                )[-1]
        except IndexError:
            raise FileNotFoundError(f'Can\'t find {type_id}: {identifier} in metadata')

    def update_job(self, identifier: str, key: str, value: t.Any) -> UpdateResult:
        return self.job_collection.update_one(
            {'identifier': identifier}, {'$set': {key: value}}
        )

    def show_components(self, type_id: str, **kwargs) -> t.List[t.Union[t.Any, str]]:
        return self.object_collection.distinct(
            'identifier', {'type_id': type_id, **kwargs}
        )

    def show_component_versions(
        self, type_id: str, identifier: str
    ) -> t.List[t.Union[t.Any, int]]:
        return self.object_collection.distinct(
            'version', {'type_id': type_id, 'identifier': identifier}
        )

    def list_components_in_scope(self, scope: str):
        out = []
        for r in self.object_collection.find({'parent': scope}):
            out.append((r['type_id'], r['identifier']))
        return out

    def show_jobs(self, status=None):
        status = {} if status is None else {'status': status}
        return list(
            self.job_collection.find(
                status, {'identifier': 1, '_id': 0, 'method': 1, 'status': 1, 'time': 1}
            )
        )

    def _component_used(
        self, type_id: str, identifier: str, version: t.Optional[int] = None
    ) -> bool:
        if version is None:
            members: t.Union[t.Dict, str] = {'$regex': f'^{identifier}/{type_id}'}
        else:
            members = Component.make_unique_id(type_id, identifier, version)

        return bool(self.object_collection.count_documents({'members': members}))

    def component_has_parents(self, type_id: str, identifier: str) -> int:
        doc = {'child': {'$regex': f'^{type_id}/{identifier}/'}}
        return self.parent_child_mappings.count_documents(doc)

    def component_version_has_parents(
        self, type_id: str, identifier: str, version: int
    ) -> int:
        doc = {'child': Component.make_unique_id(type_id, identifier, version)}
        return self.parent_child_mappings.count_documents(doc)

    def delete_component_version(
        self, type_id: str, identifier: str, version: int
    ) -> DeleteResult:
        if self._component_used(type_id, identifier, version=version):
            raise Exception('Component version already in use in other components!')

        self.parent_child_mappings.delete_many(
            {'parent': Component.make_unique_id(type_id, identifier, version)}
        )

        return self.object_collection.delete_many(
            {
                'identifier': identifier,
                'type_id': type_id,
                'version': version,
            }
        )

    def _get_component(
        self,
        type_id: str,
        identifier: str,
        version: int,
        allow_hidden: bool = False,
    ) -> t.Dict[str, t.Any]:
        if not allow_hidden:
            r = self.object_collection.find_one(
                {
                    '$or': [
                        {
                            'identifier': identifier,
                            'type_id': type_id,
                            'version': version,
                            'hidden': False,
                        },
                        {
                            'identifier': identifier,
                            'type_id': type_id,
                            'version': version,
                            'hidden': {'$exists': 0},
                        },
                    ]
                }
            )
        else:
            r = self.object_collection.find_one(
                {
                    'identifier': identifier,
                    'type_id': type_id,
                    'version': version,
                },
            )
        return r

    def get_component_version_parents(self, unique_id: str) -> t.List[str]:
        return [
            r['parent'] for r in self.parent_child_mappings.find({'child': unique_id})
        ]

    def _replace_object(
        self,
        info: t.Dict[str, t.Any],
        identifier: str,
        type_id: str,
        version: int,
    ) -> None:
        self.object_collection.replace_one(
            {'identifier': identifier, 'type_id': type_id, 'version': version},
            info,
        )

    def _update_object(
        self,
        identifier: str,
        type_id: str,
        key: str,
        value: t.Any,
        version: int,
    ):
        return self.object_collection.update_one(
            {'identifier': identifier, 'type_id': type_id, 'version': version},
            {'$set': {key: value}},
        )

    def write_output_to_job(self, identifier, msg, stream):
        if stream not in ('stdout', 'stderr'):
            raise ValueError(f'stream is "{stream}", should be stdout or stderr')
        self.job_collection.update_one(
            {'identifier': identifier}, {'$push': {stream: msg}}
        )

    def hide_component_version(
        self, type_id: str, identifier: str, version: int
    ) -> None:
        self.object_collection.update_one(
            {'type_id': type_id, 'identifier': identifier, 'version': version},
            {'$set': {'hidden': True}},
        )
