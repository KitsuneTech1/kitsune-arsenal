"""Generate an MCP manifest from the registry.

Run `python -m app.mcp` to print the tool manifest that gets registered under kitsune-hub. The
access class on each tool maps to the hub's read/write/destructive dispatcher so annotations are
never guessed.
"""
import json

from . import registry
from .tools import builtin  # noqa: F401  (registers tools)


def manifest() -> dict:
    return {
        "name": "kitsune-gateway",
        "version": "0.1.0",
        "tools": [
            {
                "name": t.name,
                "description": t.summary,
                "access": t.access,
                "inputSchema": {
                    "type": "object",
                    "properties": {k: {"type": "string", "description": v} for k, v in t.params.items()},
                },
            }
            for t in registry.all_tools()
        ],
    }


if __name__ == "__main__":
    print(json.dumps(manifest(), indent=2))
