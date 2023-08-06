from nebari.hookspecs import NebariStage, hookimpl
from typing import List

from .label_studio import LabelStudioHelmStage
from .keycloak import LabelStudioKeycloakStage

@hookimpl
def nebari_stage() -> List[NebariStage]:
    return [
        LabelStudioKeycloakStage,
        LabelStudioHelmStage,
    ]
