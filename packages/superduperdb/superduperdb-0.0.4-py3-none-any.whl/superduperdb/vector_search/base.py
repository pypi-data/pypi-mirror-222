from __future__ import annotations

import typing as t
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

import numpy
import numpy.typing
import torch

import superduperdb as s


class BaseVectorIndex:
    name: t.Optional[str] = None
    h: t.Union[torch.Tensor, numpy.ndarray, t.Sequence]
    index: t.Sequence[str]
    lookup: t.Dict[str, t.Union[t.Iterator[int], int]]
    measure: str

    def __init__(self, h, index, measure):
        if isinstance(h, list) and isinstance(h[0], torch.Tensor):
            h = torch.stack(h).numpy()
        elif isinstance(h, list) and isinstance(h[0], numpy.ndarray):
            h = numpy.stack(h)
        elif isinstance(h, list) and isinstance(h[0], list):
            h = numpy.array(h)
        elif isinstance(h, torch.Tensor):
            h = h.numpy()
        self.h = h
        self.index = index
        if index is not None:
            self.lookup = dict(zip(index, range(len(index))))
        self.measure = measure

    @property
    def shape(self):  # pragma: no cover
        return self.h.shape

    def find_nearest_from_id(self, _id, n=100):
        _ids, scores = self.find_nearest_from_ids([_id], n=n)
        return _ids[0], scores[0]

    def find_nearest_from_ids(self, _ids, n=100):
        ix = list(map(self.lookup.__getitem__, _ids))
        return self.find_nearest_from_arrays(self.h[ix, :], n=n)

    def find_nearest_from_array(self, h, n=100):
        h = to_numpy(h)
        _ids, scores = self.find_nearest_from_arrays(h[None, :], n=n)
        return _ids[0], scores[0]

    def find_nearest_from_arrays(self, h, n=100):
        raise NotImplementedError

    def __getitem__(self, item):
        raise NotImplementedError


ArrayLike = t.Union[numpy.typing.ArrayLike, torch.Tensor]


def to_numpy(x: ArrayLike) -> numpy.ndarray:
    if isinstance(x, numpy.ndarray):
        return x
    if isinstance(x, torch.Tensor):
        return x.numpy()
    return numpy.array(x)


VectorCollectionId = str
VectorCollectionItemId = str
VectorIndexMeasureType = t.Literal["l2", "dot", "css"]
VectorIndexMeasureFunction = t.Callable[[numpy.ndarray, numpy.ndarray], float]
VectorIndexMeasure = t.Union[VectorIndexMeasureType, VectorIndexMeasureFunction]


class VectorCollectionItemNotFound(Exception):
    pass


@dataclass(frozen=True)
class VectorCollectionConfig:
    id: VectorCollectionId
    dimensions: int
    measure: VectorIndexMeasure = "l2"
    parameters: t.Mapping[str, t.Any] = field(default_factory=dict)


@dataclass(frozen=True)
class VectorCollectionItem:
    id: VectorCollectionItemId
    vector: numpy.ndarray

    @classmethod
    def create(
        cls, *, id: VectorCollectionItemId, vector: ArrayLike
    ) -> VectorCollectionItem:
        return VectorCollectionItem(id=id, vector=to_numpy(vector))

    def to_dict(self) -> t.Dict:
        return {'id': self.id, 'vector': self.vector}


@dataclass(frozen=True)
class VectorCollectionResult:
    id: VectorCollectionItemId
    score: float


class VectorCollection(ABC):
    """A vector collection within a vector database.

    Concrete implementations of this class are responsible for lifecycle management of
    a single vector collection within a specific vector database.

    It is assumed that a vector collection is associated with a single vector column or
    field within a vector database.
    """

    @abstractmethod
    def add(self, items: t.Sequence[VectorCollectionItem]) -> None:
        """Add items to the collection."""
        pass

    @abstractmethod
    def find_nearest_from_id(
        self,
        identifier: VectorCollectionItemId,
        *,
        within_ids: t.Sequence[VectorCollectionItemId] = (),
        limit: int = 100,
        offset: int = 0,
    ) -> t.List[VectorCollectionResult]:
        """Find items that are nearest to the item with the given identifier."""
        pass

    @abstractmethod
    def find_nearest_from_array(
        self,
        array: ArrayLike,
        *,
        within_ids: t.Sequence[VectorCollectionItemId] = (),
        limit: int = 100,
        offset: int = 0,
    ) -> t.List[VectorCollectionResult]:
        """Find items that are nearest to the given vector."""
        pass


class VectorDatabase(ABC):
    """A manager for vector indexes within a vector database.
    A vector database that manages indexed vector collections.

    Concrete implementations of this class are responsible for lifecycle management of
    vector collections within a specific vector database.

    Clients of this class retrieve vector collections by their identifier for subsequent
    operations.
    """

    def __init__(self, *, config: s.config.VectorSearch) -> None:
        self._config = config

    @abstractmethod
    def get_table(self, config: VectorCollectionConfig) -> VectorCollection:
        """Get a vector collection by its identifier.

        :param config: configuration for the vector database
        :param create: create the table if it does not exist
        """
