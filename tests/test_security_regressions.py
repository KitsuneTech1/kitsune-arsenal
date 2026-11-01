import ipaddress
import socket
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route

import arsenal_mcp
from app.main import app
from app.mcp import manifest
from app.tools import builtin


def test_gateway_does_not_return_backend_exception_details(monkeypatch):
    def fail(*args, **kwargs):
        raise RuntimeError("provider secret must stay server-side")

    monkeypatch.setattr(builtin.httpx, "get", fail)

    response = TestClient(app).post("/call/geocode", json={"query": "synthetic"})

    assert response.status_code == 502
    assert response.json() == {"detail": "backend error"}


def test_gateway_rejects_malformed_json_before_running_a_tool():
    response = TestClient(app).post(
        "/call/now", content=b"{not-json", headers={"content-type": "application/json"}
    )

    assert response.status_code == 400
    assert response.json() == {"detail": "body must be valid JSON object of params"}


def test_gateway_rejects_variable_length_hash_algorithms():
    response = TestClient(app).post(
        "/call/hash", json={"text": "hello", "algo": "shake_128"}
    )

    assert response.status_code == 400
    assert "explicit digest length" in response.json()["detail"]


def test_standalone_hash_rejects_variable_length_hash_algorithms():
    with pytest.raises(ValueError, match="explicit digest length"):
        arsenal_mcp.hash_text("hello", "shake_128")


def test_jwt_decode_normalizes_malformed_payload_errors():
    with pytest.raises(ValueError, match="not a valid JWT"):
        arsenal_mcp.jwt_decode("%%%.$$$.signature")


def test_empty_bearer_token_fails_closed(monkeypatch):
    async def health(request):
        return PlainTextResponse("ok")

    async def data(request):
        return PlainTextResponse("protected")

    base = Starlette(routes=[Route("/health", health), Route("/data", data)])
    protected = arsenal_mcp.BearerAuth(base)
    monkeypatch.setattr(arsenal_mcp, "TOKEN", "")

    response = TestClient(protected).get("/data")

    assert response.status_code == 503
    assert response.json() == {"error": "authentication is not configured"}


def test_configured_bearer_token_is_required(monkeypatch):
    async def data(request):
        return PlainTextResponse("protected")

    base = Starlette(routes=[Route("/data", data)])
    protected = arsenal_mcp.BearerAuth(base)
    monkeypatch.setattr(arsenal_mcp, "TOKEN", "synthetic-token")

    client = TestClient(protected)
    assert client.get("/data").status_code == 401
    assert client.get("/data", headers={"Authorization": "Bearer synthetic-token"}).text == "protected"


def test_public_url_validation_rejects_unspecified_resolution(monkeypatch):
    unspecified = str(ipaddress.ip_address(0))

    def fake_getaddrinfo(host, port, type=None):
        return [(socket.AF_INET, socket.SOCK_STREAM, 6, "", (unspecified, port))]

    monkeypatch.setattr(arsenal_mcp.socket, "getaddrinfo", fake_getaddrinfo)

    with pytest.raises(ValueError, match="private or non-public"):
        arsenal_mcp._validate_public_url("https://safe.example")


def test_redirects_are_validated_before_each_request(monkeypatch):
    class Response:
        def __init__(self, status_code, url, headers):
            self.status_code = status_code
            self.url = url
            self.headers = headers

    calls = []
    responses = iter([
        Response(302, "https://safe.example", {"location": "https://next.example"}),
        Response(200, "https://next.example", {}),
    ])
    monkeypatch.setattr(arsenal_mcp, "_validate_public_url", calls.append)
    monkeypatch.setattr(arsenal_mcp.httpx, "get", lambda *args, **kwargs: next(responses))

    result, history = arsenal_mcp._public_request("https://safe.example")

    assert str(result.url) == "https://next.example"
    assert [str(item.url) for item in history] == ["https://safe.example"]
    assert calls == ["https://safe.example", "https://next.example"]


def test_manifest_marks_required_parameters_and_integer_types():
    tools = {tool["name"]: tool for tool in manifest()["tools"]}

    assert tools["hash"]["inputSchema"]["required"] == ["text"]
    assert tools["uuid"]["inputSchema"]["properties"]["n"]["type"] == "integer"
    assert "required" not in tools["now"]["inputSchema"]


def test_deployment_does_not_print_the_bearer_token():
    setup = Path("deploy/setup.sh").read_text(encoding="utf-8")

    assert "echo \"TOKEN=$(grep" not in setup
    assert "cut -d= -f2" not in setup


def test_compose_services_are_not_host_published_by_default():
    compose = Path("docker-compose.yml").read_text(encoding="utf-8")

    assert "\n    ports:" not in compose
    assert compose.count("\n    expose:") == 3
