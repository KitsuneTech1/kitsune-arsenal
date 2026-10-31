"""Kitsune Capability Gateway - FastAPI front.

/tools           list every registered capability (this is what the dashboard reads)
/health          per-tool liveness
/call/{tool}     invoke a tool with a JSON body of its params

Auth is handled at the edge (Caddy + Authentik forward_auth), so the app itself stays simple.
"""
from fastapi import FastAPI, HTTPException, Request

from . import registry
from .tools import builtin  # noqa: F401  (import registers the tools)

app = FastAPI(title="Kitsune Capability Gateway", version="0.1.0")


@app.get("/tools")
def list_tools():
    return [
        {
            "name": t.name, "summary": t.summary, "category": t.category,
            "access": t.access, "params": t.params, "replaces": t.replaces,
            "cost_usd_mo": t.cost_usd_mo, "keyless": t.keyless,
        }
        for t in registry.all_tools()
    ]


@app.get("/health")
def health():
    return {"ok": True, "tools": len(registry.all_tools())}


@app.post("/call/{tool}")
async def call(tool: str, request: Request):
    spec = registry.get(tool)
    if spec is None:
        raise HTTPException(404, f"no such tool: {tool}")
    try:
        body = await request.json()
    except Exception:
        body = {}
    if not isinstance(body, dict):
        raise HTTPException(400, "body must be a JSON object of params")
    try:
        return {"tool": tool, "result": spec.run(**body)}
    except TypeError as e:
        raise HTTPException(400, f"bad params: {e}")
    except Exception as e:  # noqa: BLE001 - surface backend errors to the caller
        raise HTTPException(502, f"backend error: {e}")
