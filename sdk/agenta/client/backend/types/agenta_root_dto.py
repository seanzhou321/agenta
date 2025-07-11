# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import (
    IS_PYDANTIC_V2,
    UniversalBaseModel,
    update_forward_refs,
)
from .agenta_tree_dto import AgentaTreeDto
from .root_dto import RootDto


class AgentaRootDto(UniversalBaseModel):
    root: RootDto
    trees: typing.List[AgentaTreeDto]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .span_dto import SpanDto  # noqa: E402, F401, I001

update_forward_refs(AgentaRootDto)
