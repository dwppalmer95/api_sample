from app1.models import Column
from app1.resource.base import BaseResource
from app1.resource.resource_registry import COLUMN_RESOURCE, register_resource
from app1.resource.versioning import ApiVersion


@register_resource(resource_name=COLUMN_RESOURCE, version_number=ApiVersion.V1)
class ColumnV1(BaseResource[Column]):
    height: float

    @classmethod
    def from_model(cls, column: Column) -> "ColumnV1":
        return ColumnV1(version_number=ApiVersion.V1, height=column.height)
