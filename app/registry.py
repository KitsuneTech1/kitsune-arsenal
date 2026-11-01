"""Tool registry: the single source of truth for what the gateway exposes.

A Tool is a name, a JSON-schema-ish input spec, an access class (read/write/destructive so the
MCP dispatcher can enforce it), and a `run` callable. The FastAPI app and the MCP manifest are
both generated from this list, so adding a capability is one entry here.
"""
from dataclasses import dataclass, field
from typing import Callable, Any


@dataclass
class Tool:
    name: str
    summary: str
    category: str
    access: str  # "read" | "write" | "destructive"
    params: dict[str, str]  # name -> short description
    run: Callable[..., Any]
    replaces: str = ""      # the paid product this stands in for
    cost_usd_mo: int = 0    # indicative retail of that product
    keyless: bool = True    # true = no external key/backend needed
    types: dict[str, str] = field(default_factory=dict)  # JSON Schema types by parameter name


_REGISTRY: dict[str, Tool] = {}


def register(tool: Tool) -> Tool:
    if tool.name in _REGISTRY:
        raise ValueError(f"duplicate tool: {tool.name}")
    _REGISTRY[tool.name] = tool
    return tool


def all_tools() -> list[Tool]:
    return list(_REGISTRY.values())


def get(name: str) -> Tool | None:
    return _REGISTRY.get(name)
