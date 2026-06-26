"""Tests for LiteLLM channel-level configuration."""

from __future__ import annotations

import pytest

from tagopen import llm
from tagopen.config import settings


@pytest.fixture
def capture_litellm(monkeypatch):
    captured: dict = {}

    async def fake_acompletion(**kwargs):
        captured.update(kwargs)
        return {"ok": True}

    monkeypatch.setattr(llm.litellm, "acompletion", fake_acompletion)
    return captured


@pytest.fixture
def use_tmp_data_dir(tmp_path, monkeypatch):
    monkeypatch.setattr(settings, "data_dir", tmp_path)
    monkeypatch.setattr(settings, "llm_model", "global-model")
    return tmp_path


def write_tools_toml(data_dir, channel_id: str, content: str) -> None:
    channel_dir = data_dir / "channels" / channel_id
    channel_dir.mkdir(parents=True)
    (channel_dir / "tools.toml").write_text(content)


async def test_acompletion_uses_global_model_without_channel_config(
    use_tmp_data_dir,
    capture_litellm,
):
    result = await llm.acompletion(channel_id="C123", messages=[])

    assert result == {"ok": True}
    assert capture_litellm["model"] == "global-model"
    assert "api_base" not in capture_litellm
    assert "api_key" not in capture_litellm


async def test_acompletion_injects_channel_endpoint_and_api_key(
    use_tmp_data_dir,
    capture_litellm,
    monkeypatch,
):
    write_tools_toml(
        use_tmp_data_dir,
        "C123",
        """
[llm]
model = "openai/ernie-4.5-turbo-32k"
api_base = "https://qianfan.baidubce.com/v2"
api_key_env = "QIANFAN_API_KEY"
""",
    )
    monkeypatch.setenv("QIANFAN_API_KEY", "secret-key")

    await llm.acompletion(channel_id="C123", messages=[])

    assert capture_litellm["model"] == "openai/ernie-4.5-turbo-32k"
    assert capture_litellm["api_base"] == "https://qianfan.baidubce.com/v2"
    assert capture_litellm["api_key"] == "secret-key"


async def test_acompletion_fails_when_api_key_env_is_missing(
    use_tmp_data_dir,
    capture_litellm,
):
    write_tools_toml(
        use_tmp_data_dir,
        "C123",
        """
[llm]
model = "openai/ernie-4.5-turbo-32k"
api_base = "https://qianfan.baidubce.com/v2"
api_key_env = "MISSING_QIANFAN_API_KEY"
""",
    )

    with pytest.raises(ValueError) as exc_info:
        await llm.acompletion(channel_id="C123", messages=[])

    message = str(exc_info.value)
    assert "MISSING_QIANFAN_API_KEY" in message
    assert "C123" in message
    assert capture_litellm == {}


async def test_acompletion_keeps_explicit_kwargs(
    use_tmp_data_dir,
    capture_litellm,
    monkeypatch,
):
    write_tools_toml(
        use_tmp_data_dir,
        "C123",
        """
[llm]
model = "openai/ernie-4.5-turbo-32k"
api_base = "https://qianfan.baidubce.com/v2"
api_key_env = "QIANFAN_API_KEY"
""",
    )
    monkeypatch.setenv("QIANFAN_API_KEY", "channel-key")

    await llm.acompletion(
        channel_id="C123",
        messages=[],
        model="explicit-model",
        api_base="https://example.invalid/v1",
        api_key="explicit-key",
    )

    assert capture_litellm["model"] == "explicit-model"
    assert capture_litellm["api_base"] == "https://example.invalid/v1"
    assert capture_litellm["api_key"] == "explicit-key"


async def test_acompletion_falls_back_when_tools_toml_is_invalid(
    use_tmp_data_dir,
    capture_litellm,
):
    write_tools_toml(use_tmp_data_dir, "C123", "[llm")

    await llm.acompletion(channel_id="C123", messages=[])

    assert capture_litellm["model"] == "global-model"
    assert "api_base" not in capture_litellm
    assert "api_key" not in capture_litellm
