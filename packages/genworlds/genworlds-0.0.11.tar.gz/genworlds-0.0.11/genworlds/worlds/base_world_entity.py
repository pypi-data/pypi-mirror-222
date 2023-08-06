from enum import Enum

from pydantic import BaseModel


class EntityTypeEnum(str, Enum):
    AGENT = "AGENT"
    OBJECT = "OBJECT"
    WORLD = "WORLD"


class BaseWorldEntity(BaseModel):
    id: str
    entity_type: EntityTypeEnum
    entity_class: str
    name: str
    description: str
    held_by: str = None
