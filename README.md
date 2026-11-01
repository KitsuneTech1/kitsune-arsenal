<p align="center"><a href="https://kitsunetechnologies.org/work"><img src="https://raw.githubusercontent.com/KitsuneTech1/.github/main/assets/kitsune-banner.svg" alt="Built by Kitsune Technologies" width="760"></a></p>

# Kitsune Arsenal

A self-hosted capability gateway that wraps local utilities and free public backends, exposing them as unified HTTP/MCP APIs.

## Overview

Kitsune Arsenal is a FastAPI service that aggregates utilities across text/encoding, web/network, geolocation, and finance. Every gateway tool is either local or proxies a free public API.

## Features

- Registry-based tool system: add a tool by writing one entry
- FastAPI HTTP endpoint: `/tools` listing and `/call/{tool}` invocation
- MCP (Model Context Protocol) manifest generation for agent integration
- Optional LibreTranslate and SearXNG services in Docker Compose
- Keyless design: no proprietary API keys required for core tools

## Architecture

```
app/
  main.py           FastAPI server with HTTP endpoints
  registry.py       tool registry (name -> spec + handler)
  tools/            domain-specific tool implementations
  mcp.py            MCP manifest generation
arsenal_mcp.py      Standalone MCP server with 27 tools
docker-compose.yml
requirements.txt
.env.example
```

## Getting Started

### Local Development

```bash
python -m pip install -r requirements.txt
python -m uvicorn app.main:app
```

Visit http://localhost:8000/tools to see available capabilities.

### Docker

```bash
cp .env.example .env
docker compose up
```

In PowerShell, use `Copy-Item .env.example .env` instead of `cp`.

Optional backends (libretranslate, searxng) can be started with:

```bash
docker compose --profile lang --profile web up
```

The optional services are included in the Compose file, but the current gateway tools do not call them.

### Standalone MCP Server

The `arsenal_mcp.py` runs as a standalone MCP endpoint:

```bash
python -m pip install -r requirements-mcp.txt
# macOS or Linux
ARSENAL_MCP_TOKEN=replace-with-a-token python arsenal_mcp.py
```

In PowerShell:

```powershell
$env:ARSENAL_MCP_TOKEN = "replace-with-a-token"
python arsenal_mcp.py
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

MIT. Copyright (c) 2025-2026 Kitsune Technologies LLC. Do what you like with it, commercially or otherwise, just keep the copyright notice. Full text in [LICENSE](LICENSE).

---

<p align="center"><sub>Part of <b>Buildtober 2026</b>: 31 open source projects in 31 days. Built by <a href="https://kitsunetechnologies.org/work">Kitsune Technologies</a>. More at <a href="https://github.com/KitsuneTech1">github.com/KitsuneTech1</a>.</sub></p>
