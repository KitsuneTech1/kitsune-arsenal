"""Generate an MCP manifest from the registry.

Run `python -m app.mcp` to print the tool manifest that gets registered under kitsune-hub. The
access class on each tool maps to the hub's read/write/destructive dispatcher so annotations are
never guessed.
"""
import json
from inspect import Parameter, signature

from . import registry
from .tools import builtin  # noqa: F401  (registers tools)


def manifest() -> dict:
    return {
        "name": "kitsune-gateway",
        "version": "0.1.0",
        "tools": [
            _tool_manifest(t)
            for t in registry.all_tools()
        ],
    }


def _tool_manifest(t: registry.Tool) -> dict:
    params = signature(t.run).parameters
    properties = {
        name: {
            "type": t.types.get(name, "string"),
            "description": description,
        }
        for name, description in t.params.items()
    }
    required = [
        name for name in t.params
        if name in params and params[name].default is Parameter.empty
    ]
    schema = {"type": "object", "properties": properties}
    if required:
        schema["required"] = required
    return {
        "name": t.name,
        "description": t.summary,
        "access": t.access,
        "inputSchema": schema,
    }


if __name__ == "__main__":
    print(json.dumps(manifest(), indent=2))
