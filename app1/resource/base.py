from abc import abstractmethod
from typing import Generic, TypeVar

from django.db import models
from pydantic import BaseModel
from typing_extensions import Self

from app1.resource.versioning import ApiVersion


ModelType = TypeVar("ModelType", bound=models.Model)


class BaseResource(Generic[ModelType], BaseModel):
    version_number: ApiVersion

    @classmethod
    @abstractmethod
    def from_model(cls, model: ModelType) -> Self:
        raise NotImplemented
