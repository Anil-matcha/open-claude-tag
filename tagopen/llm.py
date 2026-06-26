"""LiteLLM helpers — key injection, model resolution, per-channel overrides.

LiteLLM reads provider keys from os.environ, not from arbitrary Python objects.
Call configure() once at startup to sync settings → os.environ.

Per-channel model override: add a line to CHANNEL.md frontmatter:
    llm_model: gpt-4o
or set LLM_MODEL per channel in tools.toml:
    [llm]
    model = "gpt-4o"
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass

import litellm
import toml

from tagopen.config import settings

logger = logging.getLogger(__name__)

# Suppress LiteLLM's verbose success logs
litellm.suppress_debug_info = True


@dataclass(frozen=True)
class ChannelLLMConfig:
    model: str | None = None
    api_base: str | None = None
    api_key_env: str | None = None


def configure() -> None:
    """Sync API keys from settings → os.environ so LiteLLM can pick them up."""
    _set_if_nonempty("ANTHROPIC_API_KEY", settings.anthropic_api_key)
    _set_if_nonempty("OPENAI_API_KEY", settings.openai_api_key)
    _set_if_nonempty("GEMINI_API_KEY", settings.gemini_api_key)
    _set_if_nonempty("GROQ_API_KEY", settings.groq_api_key)

    logger.info("LLM configured — default model: %s", settings.llm_model)
    _log_available_providers()


def _set_if_nonempty(env_var: str, value: str) -> None:
    if value and not os.environ.get(env_var):
        os.environ[env_var] = value


def _log_available_providers() -> None:
    providers = []
    if os.environ.get("ANTHROPIC_API_KEY"):
        providers.append("Anthropic")
    if os.environ.get("OPENAI_API_KEY"):
        providers.append("OpenAI")
    if os.environ.get("GEMINI_API_KEY"):
        providers.append("Gemini")
    if os.environ.get("GROQ_API_KEY"):
        providers.append("Groq")
    if providers:
        logger.info("Available LLM providers: %s", ", ".join(providers))
    else:
        logger.warning("No LLM provider API keys found — set at least one in .env")


def resolve_model(channel_id: str | None = None) -> str:
    """Return the model to use, respecting per-channel overrides.

    Override order (highest wins):
      1. tools.toml [llm] model = "..." in channel dir
      2. LLM_MODEL env var / settings.llm_model
    """
    if channel_id:
        config = _channel_llm_config(channel_id)
        if config.model:
            return config.model
    return settings.llm_model


def _channel_llm_config(channel_id: str) -> ChannelLLMConfig:
    tools_toml = settings.channels_dir / channel_id / "tools.toml"
    if not tools_toml.exists():
        return ChannelLLMConfig()
    try:
        config = toml.loads(tools_toml.read_text())
        llm_config = config.get("llm", {})
        return ChannelLLMConfig(
            model=llm_config.get("model") or None,
            api_base=llm_config.get("api_base") or None,
            api_key_env=llm_config.get("api_key_env") or None,
        )
    except Exception:
        return ChannelLLMConfig()


def _apply_channel_llm_config(kwargs: dict, channel_id: str | None) -> None:
    if not channel_id:
        kwargs.setdefault("model", settings.llm_model)
        return

    config = _channel_llm_config(channel_id)
    kwargs.setdefault("model", config.model or settings.llm_model)

    if config.api_base:
        kwargs.setdefault("api_base", config.api_base)

    if config.api_key_env:
        api_key = os.environ.get(config.api_key_env)
        if not api_key:
            raise ValueError(
                f"Channel {channel_id} config references missing environment "
                f"variable {config.api_key_env!r} for LLM api_key"
            )
        kwargs.setdefault("api_key", api_key)


async def acompletion(channel_id: str | None = None, **kwargs):
    """Thin wrapper around litellm.acompletion that injects the resolved model."""
    _apply_channel_llm_config(kwargs, channel_id)
    return await litellm.acompletion(**kwargs)
