from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_and_tools_are_available_without_network():
    health = client.get("/health")
    tools = client.get("/tools")

    assert health.status_code == 200
    assert health.json()["ok"] is True
    assert health.json()["tools"] == 7
    assert tools.status_code == 200
    assert {tool["name"] for tool in tools.json()} == {
        "qr_code", "hash", "uuid", "slugify", "now", "geocode", "fx_rate"
    }


def test_call_runs_a_pure_tool_without_network():
    response = client.post("/call/hash", json={"text": "hello", "algo": "sha256"})

    assert response.status_code == 200
    assert response.json() == {
        "tool": "hash",
        "result": {
            "algo": "sha256",
            "hex": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",
        },
    }


def test_bad_tool_arguments_are_client_errors():
    response = client.post("/call/hash", json={"text": "hello", "algo": "not-an-algorithm"})

    assert response.status_code == 400
    assert response.json()["detail"].startswith("bad params:")


def test_unknown_tool_is_not_a_backend_error():
    response = client.post("/call/missing", json={})

    assert response.status_code == 404

