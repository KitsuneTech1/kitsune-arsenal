# Kitsune Arsenal

A self-hosted capability gateway that wraps open-source and free public backends, exposing them as unified HTTP/MCP APIs.

## Overview

Kitsune Arsenal is a FastAPI service that aggregates utilities across text/encoding, web/network, geolocation, and finance. Every tool is either a pure function (no dependencies) or proxies a free public API.

## Features

- Registry-based tool system: add a tool by writing one entry
- FastAPI HTTP endpoint: `/tools` listing and `/call/{tool}` invocation
- MCP (Model Context Protocol) manifest generation for agent integration
- Self-hosted backend support via Docker Compose (libretranslate, searxng, etc.)
- Keyless design: no proprietary API keys required for core tools

## Architecture

```
app/
  main.py           FastAPI server with HTTP endpoints
  registry.py       tool registry (name -> spec + handler)
  tools/            domain-specific tool implementations
  mcp.py            MCP manifest generation
arsenal_mcp.py      Standalone MCP server with 28+ tools
docker-compose.yml
requirements.txt
.env.example
```

## Getting Started

### Local Development

```bash
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Visit http://localhost:8000/tools to see available capabilities.

### Docker

```bash
docker compose up
```

Optional backends (libretranslate, searxng) can be started with:

```bash
docker compose --profile lang --profile web up
```

### Standalone MCP Server

The `arsenal_mcp.py` runs as a standalone MCP endpoint:

```bash
ARSENAL_MCP_TOKEN=<token> python arsenal_mcp.py
```

Endpoint at `http://localhost:8810/mcp` with `Authorization: Bearer <token>`.

## Tools Included

- **Text & Encoding**: hash, UUID, slugify, base64/URL encoding, JSON validation/diffing
- **Web & Network**: QR codes, URL expansion, HTTP headers, DNS, WHOIS, TLS certs, IP geolocation
- **Geo & Finance**: geocoding, reverse geocoding, FX rates, cron parsing
- **Utilities**: time, TOTP, JWT decode, passwords, color conversion, regex testing, entity extraction

## Adding Tools

Add a new tool to `app/tools/` or to the registry:

```python
register(Tool(
    name="my_tool",
    summary="Brief description",
    category="Category",
    access="read",
    params={"param1": "description"},
    run=lambda param1: {"result": ...},
))
```

The MCP manifest and HTTP listing update automatically.

## Deployment

Deploy behind Caddy with forward_auth for edge authentication. The app itself assumes auth is handled upstream.

## License

MIT
