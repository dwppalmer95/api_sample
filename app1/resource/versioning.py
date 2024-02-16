from django.db.models import TextChoices
from pydantic import BaseModel


class ApiVersion(TextChoices):
    V1 = "v1"
    V2 = "v2"


class VersionResource(BaseModel):
    version: ApiVersion