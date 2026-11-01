import pytest

from arsenal_mcp import base64_tool, color_convert, url_encode


def test_base64_round_trip():
    encoded = base64_tool("hello")

    assert encoded == {"result": "aGVsbG8="}
    assert base64_tool(encoded["result"], mode="decode") == {"result": "hello"}


def test_base64_decode_rejects_invalid_characters():
    with pytest.raises(ValueError, match="not valid base64"):
        base64_tool("%%%", mode="decode")


@pytest.mark.parametrize("tool", [base64_tool, url_encode])
def test_encoding_tools_reject_unknown_modes(tool):
    with pytest.raises(ValueError, match="mode must be encode or decode"):
        tool("hello", mode="other")


def test_color_convert_rejects_out_of_range_rgb_values():
    with pytest.raises(ValueError, match="between 0 and 255"):
        color_convert("256,0,0")


def test_color_convert_returns_normalized_values():
    assert color_convert("#abc") == {
        "hex": "#aabbcc",
        "rgb": "170,187,204",
        "r": 170,
        "g": 187,
        "b": 204,
    }


def test_password_generation_rejects_unknown_kind():
    from arsenal_mcp import password_gen

    with pytest.raises(ValueError, match="kind must be password or passphrase"):
        password_gen(kind="unknown")
