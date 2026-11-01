"""First batch of real, keyless capabilities.

Pure-function tools cost nothing to keep online; the two network tools proxy free public
services (OSM Nominatim, ECB) rather than a paid API. This is the pattern every later tool follows.
"""
import base64
import hashlib
import io
import json
import uuid as _uuid
from datetime import datetime, timezone

import httpx
import qrcode
from slugify import slugify as _slugify

from ..registry import Tool, register


# --- pure functions (zero backend) -----------------------------------------

def _qr(text: str) -> dict:
    img = qrcode.make(text)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return {"png_base64": base64.b64encode(buf.getvalue()).decode()}


def _hash(text: str, algo: str = "sha256") -> dict:
    if algo not in hashlib.algorithms_available:
        raise ValueError(f"unknown algo: {algo}")
    digest = hashlib.new(algo, text.encode())
    try:
        value = digest.hexdigest()
    except TypeError as e:
        raise ValueError(f"algorithm requires an explicit digest length: {algo}") from e
    return {"algo": algo, "hex": value}


def _uuid_gen(n: int = 1) -> dict:
    n = max(1, min(int(n), 100))
    return {"uuids": [str(_uuid.uuid4()) for _ in range(n)]}


def _slug(text: str) -> dict:
    return {"slug": _slugify(text)}


def _now() -> dict:
    t = datetime.now(timezone.utc)
    return {"iso": t.isoformat(), "epoch": int(t.timestamp())}


# --- free public backends (no paid key) ------------------------------------

def _geocode(query: str) -> dict:
    r = httpx.get(
        "https://nominatim.openstreetmap.org/search",
        params={"q": query, "format": "json", "limit": 1},
        headers={"User-Agent": "kitsune-gateway/0.1"},
        timeout=15,
    )
    r.raise_for_status()
    hits = r.json()
    if not hits:
        return {"found": False}
    h = hits[0]
    return {"found": True, "lat": float(h["lat"]), "lon": float(h["lon"]), "label": h["display_name"]}


def _fx(base: str = "USD", quote: str = "EUR") -> dict:
    # ECB daily reference rates, free.
    r = httpx.get("https://api.frankfurter.dev/v1/latest", params={"base": base, "symbols": quote}, timeout=15)
    r.raise_for_status()
    data = r.json()
    return {"base": base, "quote": quote, "rate": data["rates"][quote], "date": data["date"]}


def _register_all() -> None:
    register(Tool("qr_code", "Generate a QR code PNG for any text or URL.", "Comms & Productivity",
                  "read", {"text": "content to encode"}, lambda text: _qr(text),
                  replaces="QR Code API", cost_usd_mo=20))
    register(Tool("hash", "Hash text with any algorithm (sha256, md5, blake2b, ...).", "Dev & Infra",
                  "read", {"text": "input", "algo": "algorithm, default sha256"},
                  lambda text, algo="sha256": _hash(text, algo)))
    register(Tool("uuid", "Generate one or more UUID v4s.", "Dev & Infra",
                  "read", {"n": "how many, 1-100"}, lambda n=1: _uuid_gen(n),
                  types={"n": "integer"}))
    register(Tool("slugify", "Turn any string into a URL-safe slug.", "Dev & Infra",
                  "read", {"text": "input"}, lambda text: _slug(text)))
    register(Tool("now", "Current UTC time as ISO and epoch.", "Dev & Infra",
                  "read", {}, lambda: _now()))
    register(Tool("geocode", "Address or place -> lat/lon via OpenStreetMap.", "Geo & Maps",
                  "read", {"query": "address or place name"}, lambda query: _geocode(query),
                  replaces="Google Maps Geocoding", cost_usd_mo=200))
    register(Tool("fx_rate", "Live FX rate between two currencies (ECB).", "Finance & Data",
                  "read", {"base": "e.g. USD", "quote": "e.g. EUR"},
                  lambda base="USD", quote="EUR": _fx(base, quote),
                  replaces="paid FX APIs", cost_usd_mo=15))


_register_all()
