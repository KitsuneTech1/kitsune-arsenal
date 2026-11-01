"""Kitsune Arsenal - standalone MCP server.

Its own MCP endpoint (streamable HTTP + bearer), deliberately NOT behind kitsune-hub.
Each tool is a keyless capability or proxies a free public backend, so the box costs almost
nothing to keep online. Add more tools by writing another @mcp.tool below; the schema comes from
the type hints.

Run:  ARSENAL_MCP_TOKEN=... python arsenal_mcp.py
Serves POST/GET at http://<host>:8810/mcp  (Authorization: Bearer <token>)
"""
from __future__ import annotations

import base64
import binascii
import difflib
import hashlib
import io
import json
import os
import re
import secrets
import socket
import ssl
import string
import uuid as _uuid
from datetime import datetime, timezone
from urllib.parse import quote, unquote

import httpx
from mcp.server.fastmcp import FastMCP
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse, PlainTextResponse
from starlette.routing import Route

TOKEN = os.environ.get("ARSENAL_MCP_TOKEN", "")
PORT = int(os.environ.get("ARSENAL_MCP_PORT", "8810"))
UA = {"User-Agent": "kitsune-arsenal/0.1"}

mcp = FastMCP("kitsune-arsenal", host="0.0.0.0", port=PORT)


# ============================ text, data, encoding ============================

@mcp.tool()
def now() -> dict:
    """Current UTC time as ISO 8601 and epoch seconds."""
    t = datetime.now(timezone.utc)
    return {"iso": t.isoformat(), "epoch": int(t.timestamp())}


@mcp.tool()
def uuid(n: int = 1) -> dict:
    """Generate n UUID v4 values (1-100)."""
    n = max(1, min(int(n), 100))
    return {"uuids": [str(_uuid.uuid4()) for _ in range(n)]}


@mcp.tool()
def hash_text(text: str, algo: str = "sha256") -> dict:
    """Hash text with any hashlib algorithm (sha256, sha1, md5, blake2b, sha3_256...)."""
    if algo not in hashlib.algorithms_available:
        raise ValueError(f"unknown algo: {algo}")
    return {"algo": algo, "hex": hashlib.new(algo, text.encode()).hexdigest()}


@mcp.tool()
def slugify(text: str) -> dict:
    """Turn a string into a lowercase URL-safe slug."""
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return {"slug": s}


@mcp.tool()
def base64_tool(text: str, mode: str = "encode") -> dict:
    """Base64 encode or decode UTF-8 text. mode = encode | decode."""
    if mode == "encode":
        return {"result": base64.b64encode(text.encode()).decode()}
    if mode != "decode":
        raise ValueError("mode must be encode or decode")
    try:
        return {"result": base64.b64decode(text).decode("utf-8", "replace")}
    except binascii.Error as e:
        raise ValueError(f"not valid base64: {e}")


@mcp.tool()
def url_encode(text: str, mode: str = "encode") -> dict:
    """URL percent-encode or decode text. mode = encode | decode."""
    if mode == "encode":
        return {"result": quote(text)}
    if mode == "decode":
        return {"result": unquote(text)}
    raise ValueError("mode must be encode or decode")


@mcp.tool()
def json_format(text: str, minify: bool = False) -> dict:
    """Validate and pretty-print (or minify) a JSON string."""
    obj = json.loads(text)
    out = json.dumps(obj, separators=(",", ":")) if minify else json.dumps(obj, indent=2, sort_keys=True)
    return {"valid": True, "result": out}


@mcp.tool()
def json_diff(a: str, b: str) -> dict:
    """Diff two JSON objects. Returns added, removed, and changed top-level keys (deep for nested equality)."""
    da, db = json.loads(a), json.loads(b)
    if not (isinstance(da, dict) and isinstance(db, dict)):
        raise ValueError("both inputs must be JSON objects")
    added = {k: db[k] for k in db if k not in da}
    removed = {k: da[k] for k in da if k not in db}
    changed = {k: {"from": da[k], "to": db[k]} for k in da if k in db and da[k] != db[k]}
    return {"added": added, "removed": removed, "changed": changed}


@mcp.tool()
def text_diff(a: str, b: str) -> dict:
    """Unified diff between two blocks of text."""
    diff = difflib.unified_diff(a.splitlines(), b.splitlines(), lineterm="", n=2)
    return {"diff": "\n".join(diff)}


@mcp.tool()
def regex_test(pattern: str, text: str, flags: str = "") -> dict:
    """Test a regex against text. flags: any of i,m,s. Returns up to 100 matches with groups."""
    f = 0
    f |= re.I if "i" in flags else 0
    f |= re.M if "m" in flags else 0
    f |= re.S if "s" in flags else 0
    matches = [{"match": m.group(0), "groups": list(m.groups()), "span": m.span()}
               for m in list(re.finditer(pattern, text, f))[:100]]
    return {"count": len(matches), "matches": matches}


@mcp.tool()
def extract_entities(text: str) -> dict:
    """Pull emails, URLs, and phone-like numbers out of free text."""
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    urls = re.findall(r"https?://[^\s<>\"')]+", text)
    phones = re.findall(r"(?:(?:\+\d{1,3}[\s-]?)?(?:\(\d{1,4}\)[\s-]?)?\d[\d\s-]{6,}\d)", text)
    return {"emails": sorted(set(emails)), "urls": sorted(set(urls)),
            "phones": sorted(set(p.strip() for p in phones))}


@mcp.tool()
def token_count(text: str) -> dict:
    """Approximate LLM token count (heuristic: ~4 chars/token, blended with word count)."""
    chars = len(text)
    words = len(text.split())
    est = round((chars / 4 + words * 1.3) / 2)
    return {"chars": chars, "words": words, "approx_tokens": est,
            "note": "heuristic estimate, not a real tokenizer"}


@mcp.tool()
def color_convert(color: str) -> dict:
    """Convert a color between hex and rgb. Accepts '#rrggbb' or 'r,g,b'."""
    c = color.strip().lstrip("#")
    if "," in color:
        r, g, b = (int(x) for x in color.split(","))
    else:
        if len(c) == 3:
            c = "".join(ch * 2 for ch in c)
        r, g, b = int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16)
    if any(value < 0 or value > 255 for value in (r, g, b)):
        raise ValueError("RGB values must be between 0 and 255")
    return {"hex": f"#{r:02x}{g:02x}{b:02x}", "rgb": f"{r},{g},{b}", "r": r, "g": g, "b": b}


@mcp.tool()
def password_gen(length: int = 20, kind: str = "password") -> dict:
    """Generate a strong password (kind=password) or a passphrase (kind=passphrase)."""
    if kind == "passphrase":
        words = ["fox", "river", "amber", "quartz", "cedar", "harbor", "lantern", "signal",
                 "orbit", "meadow", "cinder", "willow", "pixel", "onyx", "saffron", "delta"]
        n = max(3, min(int(length), 12))
        return {"value": "-".join(secrets.choice(words) for _ in range(n)) + str(secrets.randbelow(100))}
    length = max(8, min(int(length), 128))
    alpha = string.ascii_letters + string.digits + "!@#$%^&*-_=+"
    return {"value": "".join(secrets.choice(alpha) for _ in range(length))}


@mcp.tool()
def jwt_decode(token: str) -> dict:
    """Decode a JWT header and payload without verifying the signature."""
    parts = token.split(".")
    if len(parts) < 2:
        raise ValueError("not a JWT")

    def _d(seg: str):
        seg += "=" * (-len(seg) % 4)
        return json.loads(base64.urlsafe_b64decode(seg))

    return {"header": _d(parts[0]), "payload": _d(parts[1]), "signature_verified": False}


# ============================ web, network, dns ============================

@mcp.tool()
def qr_code(text: str) -> dict:
    """Generate a QR code for text or a URL, returned as a base64 PNG."""
    import qrcode  # local import so the tool degrades gracefully if pillow is missing
    buf = io.BytesIO()
    qrcode.make(text).save(buf, format="PNG")
    return {"png_base64": base64.b64encode(buf.getvalue()).decode()}


@mcp.tool()
def url_expand(url: str) -> dict:
    """Follow redirects and return the final URL plus the redirect chain."""
    r = httpx.get(url, follow_redirects=True, headers=UA, timeout=15)
    return {"final_url": str(r.url), "status": r.status_code,
            "chain": [str(h.url) for h in r.history]}


@mcp.tool()
def http_headers(url: str) -> dict:
    """Fetch the HTTP response headers for a URL."""
    r = httpx.get(url, follow_redirects=True, headers=UA, timeout=15)
    return {"status": r.status_code, "final_url": str(r.url), "headers": dict(r.headers)}


@mcp.tool()
def dns_lookup(name: str, record: str = "A") -> dict:
    """Resolve a DNS record (A, AAAA, MX, TXT, NS, CNAME) for a hostname."""
    import dns.resolver
    answers = dns.resolver.resolve(name, record)
    return {"name": name, "type": record, "records": [r.to_text() for r in answers]}


@mcp.tool()
def whois_domain(domain: str) -> dict:
    """Domain registration info via RDAP (free). Returns registrar, key dates, and status."""
    r = httpx.get(f"https://rdap.org/domain/{domain}", headers=UA, timeout=15, follow_redirects=True)
    r.raise_for_status()
    d = r.json()
    events = {e.get("eventAction"): e.get("eventDate") for e in d.get("events", [])}
    return {"handle": d.get("handle"), "status": d.get("status", []),
            "registration": events.get("registration"), "expiration": events.get("expiration"),
            "last_changed": events.get("last changed")}


@mcp.tool()
def ssl_cert_check(host: str, port: int = 443) -> dict:
    """Check a TLS certificate's issuer and expiry for host:port."""
    ctx = ssl.create_default_context()
    with socket.create_connection((host, int(port)), timeout=12) as sock:
        with ctx.wrap_socket(sock, server_hostname=host) as ss:
            cert = ss.getpeercert()
    not_after = cert.get("notAfter")
    exp = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z").replace(tzinfo=timezone.utc)
    days = (exp - datetime.now(timezone.utc)).days
    issuer = dict(x[0] for x in cert.get("issuer", []))
    return {"host": host, "expires": not_after, "days_left": days,
            "issuer": issuer.get("organizationName"), "expired": days < 0}


@mcp.tool()
def ip_info(ip: str) -> dict:
    """Geolocation and network owner for an IP address (free ip-api.com)."""
    r = httpx.get(f"http://ip-api.com/json/{ip}", headers=UA, timeout=12)
    r.raise_for_status()
    d = r.json()
    return {"ip": ip, "country": d.get("country"), "region": d.get("regionName"),
            "city": d.get("city"), "isp": d.get("isp"), "org": d.get("org"),
            "lat": d.get("lat"), "lon": d.get("lon")}


# ============================ geo, finance, time ============================

@mcp.tool()
def geocode(query: str) -> dict:
    """Address or place name to latitude/longitude via OpenStreetMap Nominatim."""
    r = httpx.get("https://nominatim.openstreetmap.org/search",
                  params={"q": query, "format": "json", "limit": 1}, headers=UA, timeout=15)
    r.raise_for_status()
    hits = r.json()
    if not hits:
        return {"found": False}
    h = hits[0]
    return {"found": True, "lat": float(h["lat"]), "lon": float(h["lon"]), "label": h["display_name"]}


@mcp.tool()
def reverse_geocode(lat: float, lon: float) -> dict:
    """Latitude/longitude to a human address via OpenStreetMap Nominatim."""
    r = httpx.get("https://nominatim.openstreetmap.org/reverse",
                  params={"lat": lat, "lon": lon, "format": "json"}, headers=UA, timeout=15)
    r.raise_for_status()
    d = r.json()
    return {"label": d.get("display_name"), "address": d.get("address", {})}


@mcp.tool()
def fx_rate(base: str = "USD", quote_ccy: str = "EUR") -> dict:
    """Live FX reference rate between two currencies (ECB via frankfurter.dev)."""
    r = httpx.get("https://api.frankfurter.dev/v1/latest",
                  params={"base": base, "symbols": quote_ccy}, headers=UA, timeout=15)
    r.raise_for_status()
    d = r.json()
    return {"base": base, "quote": quote_ccy, "rate": d["rates"][quote_ccy], "date": d["date"]}


@mcp.tool()
def cron_describe(expr: str, count: int = 5) -> dict:
    """Next run times for a 5-field cron expression (UTC)."""
    from croniter import croniter
    base = datetime.now(timezone.utc)
    it = croniter(expr, base)
    n = max(1, min(int(count), 20))
    return {"expr": expr, "next_runs_utc": [it.get_next(datetime).isoformat() for _ in range(n)]}


@mcp.tool()
def totp_now(secret: str) -> dict:
    """Current TOTP 6-digit code for a base32 secret (2FA)."""
    import pyotp
    return {"code": pyotp.TOTP(secret).now()}


# Note: native MCP tools/list already enumerates capabilities, so no custom lister is needed.

# ============================ transport + bearer auth ============================

class BearerAuth(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if request.url.path == "/health":
            return await call_next(request)
        if TOKEN:
            auth = request.headers.get("authorization", "")
            if auth != f"Bearer {TOKEN}":
                return JSONResponse({"error": "unauthorized"}, status_code=401)
        return await call_next(request)


def build_app():
    app = mcp.streamable_http_app()
    app.add_middleware(BearerAuth)
    app.router.routes.append(Route("/health", lambda r: PlainTextResponse("ok")))
    return app


if __name__ == "__main__":
    import uvicorn
    if not TOKEN:
        print("WARNING: ARSENAL_MCP_TOKEN is empty; server is unauthenticated.")
    uvicorn.run(build_app(), host="0.0.0.0", port=PORT)
