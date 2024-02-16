from builtins import KeyError

from app1.resource.base import BaseResource
from app1.resource.versioning import ApiVersion

COLUMN_RESOURCE = "column_resource"

RESOURCE_REGISTRY = {}


def register_resource(resource_name: str, version_number: ApiVersion):
    def register_resource_decorator(cls):
        print(f"here: {version_number}")
        resource_versions = RESOURCE_REGISTRY.get(resource_name, {})
        resource_versions[version_number] = cls
        RESOURCE_REGISTRY[resource_name] = resource_versions
        return cls
    return register_resource_decorator


class ResourceVersionException(Exception):
    pass


def get_resource(resource_name: str, version: ApiVersion) -> BaseResource:
    try:
        return RESOURCE_REGISTRY[resource_name][version]
    except KeyError:
        raise ResourceVersionException("Resource does not exist")
