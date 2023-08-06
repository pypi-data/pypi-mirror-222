from typing import Any, Annotated

from pydantic import BaseModel, model_validator, model_serializer
from sotrans_fastapi_keycloak.model import KeycloakUserBaseModel, OIDCUserBaseModel, user_model_attributes_validator, \
    user_model_attributes_serializer, KeycloakUserAttribute

KeycloakUserStrAttribute = Annotated[str | None, KeycloakUserAttribute()]


class SotransKeycloakUserInfoModel(BaseModel):
    """Represents an update Keycloak user object in SOTRANS configuration"""
    email: str | None = None
    name: KeycloakUserStrAttribute = None
    surname: KeycloakUserStrAttribute = None
    patronymic: KeycloakUserStrAttribute = None
    phone: KeycloakUserStrAttribute = None
    job_title: KeycloakUserStrAttribute = None
    status: KeycloakUserStrAttribute = None
    photo: KeycloakUserStrAttribute = None
    subsidiary_id: KeycloakUserStrAttribute = None
    organization_id: KeycloakUserStrAttribute = None
    note: KeycloakUserStrAttribute = None

    @model_validator(mode = 'before')
    @classmethod
    def validate(cls: type[BaseModel], value: Any) -> Any:
        return user_model_attributes_validator(cls, value)

    def model_dump_keycloak(self):
        return user_model_attributes_serializer(self)


class SotransKeycloakUserCreateModel(BaseModel):
    """Represents a creation Keycloak user object in SOTRANS configuration"""
    name: str
    surname: str
    patronymic: str
    phone: str
    email: str
    password: str


class SotransKeycloakUserModel(KeycloakUserBaseModel, SotransKeycloakUserInfoModel):
    """Represents a full Keycloak user object in SOTRANS configuration"""
    pass


class SotransOIDCUserModel(OIDCUserBaseModel, SotransKeycloakUserInfoModel):
    pass
