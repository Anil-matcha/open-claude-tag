# Open AI Design Agent — Open-Source Alternative to Lovart AI, Runway Agent, Luma Labs Agent, Krea Agent

> **The free, open-source AI design agent.** Plan, generate, and assemble full creative deliverables — posters, social campaigns, brand kits, ad creatives, motion ads, and video cutdowns — through an autonomous agent that orchestrates 200+ image and video models. No subscription, no credit caps, no creative restrictions.

**Community:** Join [Reddit](https://reddit.com/r/muapi) & [Discord](https://discord.gg/s7KW4fsqXK) for discussions and support

---

## ☁️ Powered by Atlas Cloud — Unified LLM + Image Generation API

<p align="center">
  <a href="https://www.atlascloud.ai/?utm_source=github&utm_medium=link&utm_campaign=Open-AI-Design-Agent">
    <img src="assets/atlas-cloud-logo.png" alt="Atlas Cloud" width="200"/>
  </a>
</p>

[**Atlas Cloud**](https://www.atlascloud.ai/?utm_source=github&utm_medium=link&utm_campaign=Open-AI-Design-Agent) gives Open-AI-Design-Agent a single API key for **both** LLM reasoning and image generation — so you can replace multiple vendor integrations with one endpoint:

- **LLM (OpenAI-compatible)** — DeepSeek, Qwen, Claude, Llama, and 50+ models via a drop-in OpenAI-format API. Use for the agent's planning loop, routing decisions, and brand-copy generation.
- **Image Generation (async API)** — gpt-image-2, Wan, Flux, Seedream, Recraft, and more via `api.atlascloud.ai`. Power your Design Studio and Motion Studio without managing separate API keys per model vendor.

**Quick configuration:**

```env
# LLM backend (OpenAI-compatible, drop-in replacement)
OPENAI_BASE_URL=https://api.atlascloud.ai/v1
OPENAI_API_KEY=<your-atlascloud-key>
OPENAI_MODEL=deepseek-ai/deepseek-v4-pro

# Image Generation (Atlas async API)
ATLAS_IMAGE_BASE=https://api.atlascloud.ai/api/v1/model
ATLAS_IMAGE_MODEL=openai/gpt-image-2/text-to-image
```

> **Note for reasoning models:** Set `max_tokens` ≥ 512 (recommended: 4096+) to avoid truncated responses from inference-heavy models like DeepSeek-v4-Pro.

Get your free API key → [Atlas Cloud Coding Plan](https://www.atlascloud.ai/console/coding-plan) · [Browse all models](https://www.atlascloud.ai/models)

<details>
<summary>📋 59 supported LLM models (click to expand)</summary>

| Model ID | Description |
|---|---|
| `deepseek-ai/deepseek-v4-pro` | DeepSeek v4 Pro — top-tier reasoning |
| `deepseek-ai/deepseek-r1` | DeepSeek R1 — chain-of-thought |
| `deepseek-ai/deepseek-v3` | DeepSeek v3 — fast & capable |
| `deepseek-ai/deepseek-r1-distill-qwen-32b` | DeepSeek R1 distilled (32B) |
| `deepseek-ai/deepseek-r1-distill-llama-70b` | DeepSeek R1 distilled (70B) |
| `qwen/qwen3-235b-a22b` | Qwen3 235B MoE |
| `qwen/qwen3-32b` | Qwen3 32B |
| `qwen/qwen3-14b` | Qwen3 14B |
| `qwen/qwen3-8b` | Qwen3 8B |
| `qwen/qwen-2.5-72b-instruct` | Qwen2.5 72B Instruct |
| `qwen/qwen-2.5-coder-32b-instruct` | Qwen2.5 Coder 32B |
| `qwen/qwq-32b` | QwQ 32B reasoning |
| `anthropic/claude-opus-4-5` | Claude Opus 4.5 |
| `anthropic/claude-sonnet-4-5` | Claude Sonnet 4.5 |
| `anthropic/claude-haiku-3-5` | Claude Haiku 3.5 |
| `openai/gpt-4o` | GPT-4o |
| `openai/gpt-4o-mini` | GPT-4o mini |
| `openai/o1-mini` | OpenAI o1-mini |
| `openai/o3-mini` | OpenAI o3-mini |
| `openai/o4-mini` | OpenAI o4-mini |
| `google/gemini-2.5-pro` | Gemini 2.5 Pro |
| `google/gemini-2.5-flash` | Gemini 2.5 Flash |
| `google/gemini-2.0-flash` | Gemini 2.0 Flash |
| `meta-llama/llama-4-scout-17b` | Llama 4 Scout 17B |
| `meta-llama/llama-4-maverick-17b` | Llama 4 Maverick 17B |
| `meta-llama/llama-3.3-70b-instruct` | Llama 3.3 70B Instruct |
| `meta-llama/llama-3.1-8b-instruct` | Llama 3.1 8B Instruct |
| `mistralai/mistral-7b-instruct` | Mistral 7B Instruct |
| `mistralai/mixtral-8x7b-instruct` | Mixtral 8x7B |
| `mistralai/mistral-large-latest` | Mistral Large |
| `microsoft/phi-4` | Phi-4 |
| `microsoft/phi-3.5-mini-128k-instruct` | Phi-3.5 Mini |
| `nvidia/llama-3.1-nemotron-70b-instruct` | Nemotron 70B |
| `amazon/nova-pro-v1` | Amazon Nova Pro |
| `amazon/nova-lite-v1` | Amazon Nova Lite |
| `amazon/nova-micro-v1` | Amazon Nova Micro |
| `cohere/command-r-plus` | Cohere Command R+ |
| `cohere/command-r` | Cohere Command R |
| `01-ai/yi-lightning` | Yi Lightning |
| `databricks/dbrx-instruct` | DBRX Instruct |
| `allenai/olmo-7b-instruct` | OLMo 7B |
| `togethercomputer/falcon-40b-instruct` | Falcon 40B |
| `huggingfaceh4/zephyr-7b-beta` | Zephyr 7B Beta |
| `openchat/openchat-3.5` | OpenChat 3.5 |
| `teknium/openhermes-2.5-mistral-7b` | OpenHermes 2.5 |
| `nousresearch/nous-hermes-2-mixtral-8x7b` | Nous Hermes 2 Mixtral |
| `nousresearch/nous-hermes-llama2-13b` | Nous Hermes Llama2 13B |
| `garage-bam/sqlcoder-7b-2` | SQLCoder 7B |
| `lmsys/vicuna-13b-v1.5` | Vicuna 13B |
| `stabilityai/stablelm-zephyr-3b` | StableLM Zephyr 3B |
| `togethercomputer/redpajama-incite-7b-chat` | RedPajama 7B Chat |
| `snorkelai/snorkel-mistral-pairrm-dpo` | Snorkel Mistral |
| `Austism/chronos-hermes-13b` | Chronos Hermes 13B |
| `DiscoResearch/DiscoLM-mixtral-8x7b-v2` | DiscoLM Mixtral |
| `Gryphe/MythoMax-L2-13b` | MythoMax L2 13B |
| `upstage/solar-10.7b-instruct-v1.0` | Solar 10.7B |
| `cognitivecomputations/dolphin-2.5-mixtral-8x7b` | Dolphin 2.5 Mixtral |
| `mistralai/mistral-medium` | Mistral Medium |
| `mistralai/mistral-small` | Mistral Small |

</details>

<details>
<summary>🎨 Supported image generation models via Atlas Cloud (click to expand)</summary>

| Model | Category |
|---|---|
| `openai/gpt-image-2/text-to-image` | Text-to-Image |
| `black-forest-labs/flux-1-pro/text-to-image` | Text-to-Image |
| `black-forest-labs/flux-1-dev/text-to-image` | Text-to-Image |
| `black-forest-labs/flux-2-pro/text-to-image` | Text-to-Image |
| `stability-ai/stable-diffusion-xl/text-to-image` | Text-to-Image |
| `bytedance/seedream-5/text-to-image` | Text-to-Image |
| `ideogram/v3/text-to-image` | Text-to-Image |
| `recraft/v3/text-to-image` | Text-to-Image |
| `kling/v2-master/image-to-video` | Image-to-Video |
| `bytedance/seedance-2-0/text-to-video` | Text-to-Video |
| `wan/v2-1/text-to-video` | Text-to-Video |

</details>

---

> 🤖 **Automate Lovart, Runway, Luma Labs, Krea, Pika & more with AI coding agents:** [Generative-Media-Skills](https://github.com/SamurAIGPT/Generative-Media-Skills) — a library of skills that let agents like **Claude Code**, **Codex**, and other coding assistants drive 200+ image/video models end-to-end (brief → plan → generate → edit → assemble) directly from your terminal. Build automated creative pipelines without touching a UI.

https://github.com/user-attachments/assets/fee3857c-887d-4c27-b3dc-a1fe9ad8f438

### Related projects

> **Open-source Freepik, Krea, Openart alternative — uncensored image & video studio with 200+ models** -> https://github.com/Anil-matcha/Open-Generative-AI

> **Open-source Weavy, Flora Fauna, Freepik Spaces, Krea Nodes alternative — visual workflow editor** -> https://github.com/SamurAIGPT/Vibe-Workflow

> **Open-source Opus Clip alternative — turn long videos into viral vertical shorts** -> https://github.com/SamurAIGPT/AI-Youtube-Shorts-Generator

> **Open-source multi-modal chatbot and Poe alternative** -> https://github.com/Anil-matcha/Open-Poe-AI

<p align="center">
  <a href="https://github.com/Anil-matcha/awesome-generative-ai-apps">
    <img src="https://img.shields.io/badge/Part%20of-Awesome%20Generative%20AI%20Apps-FFD700?style=for-the-badge&logo=github&logoColor=black" alt="Awesome Generative AI Apps">
  </a>
</p>

> 🎨 **[Explore 50+ more open-source AI apps →](https://github.com/Anil-matcha/awesome-generative-ai-apps)**

## 🌐 Try it Online — No Install Required

**Hosted version:** [https://muapi.ai/assistant](https://muapi.ai/assistant)

Run the design agent directly in your browser — no Node.js, no setup. Sign up for a free account to start designing. The hosted version is always up to date with the latest models, planners, and templates.

**Follow** the [creator](https://x.com/matchaman11) for updates

---

Open AI Design Agent is a free, open-source AI design agent that turns natural-language briefs into full creative deliverables. Instead of picking one model and generating one asset, you describe a campaign, brand, or scene and the agent plans the deliverable list, picks the best model per asset (typography, vector, photoreal, motion), generates them in dependency order, threads brand references forward, and hands back the assembled kit. Powered by [Muapi.ai](https://muapi.ai), it orchestrates 200+ image and video models — Nano Banana 2, Flux 2 Pro, Ideogram v3, Seedream 5, GPT-Image, Recraft v3, Midjourney v7, Kling, Sora, Veo, Runway, Luma Ray2 — across a single agent loop you can self-host and modify.

**Why Open Lovart instead of Lovart, Runway Agent, Luma Labs Agent, Krea Agent?**
- **Free & open-source** — MIT-licensed, no subscription, no credit caps
- **Self-hosted** — your briefs, brand kits, and outputs stay on your machine
- **200+ models orchestrated** — image *and* video, routed automatically per asset (Flux 2, Nano Banana 2, Ideogram v3, Recraft v3, Kling, Sora, Veo, Runway, Luma Ray2)
- **Inspectable agent loop** — every plan, model choice, and intermediate output is visible and editable; nothing is black-boxed
- **Brand kit conditioning** — palette, fonts, logo, and tone persist across every generation in a campaign
- **Multi-image reference** — up to 14 images for style transfer, product placement, or character consistency
- **Static + motion in one agent** — same brief produces poster, social cutdown, and 9:16 video ad without switching tools
- **Extensible** — add your own templates, models, planners, and tool-calls; fork the agent loop; ship products on top

## ✨ Features

- **Design Agent (Chat Mode)** — Describe a brand or campaign in plain English; the agent plans deliverables, picks the right model per asset, generates them in order, and assembles the kit
- **Design Studio** — Posters, flyers, ad creatives, social graphics, presentation slides, logos, brand identities, illustrations, packaging mockups, UI screens — all from one prompt or chat thread
- **Motion Studio** — Animated logos, product motion mockups, video ads, social video cutdowns (9:16 / 1:1 / 16:9), lip-synced spokesperson clips
- **Multi-Image Reference** — Up to 14 reference images for style transfer, brand consistency, or product placement (Nano Banana 2 Edit, Flux Kontext, GPT-Image Edit, Seedream Edit)
- **Text Rendering** — Auto-route prompts containing typographic copy to text-capable models (Ideogram v3, Flux Pro Ultra, Nano Banana 2, GPT-Image)
- **Edit Mode** — Refine, recolor, restyle, expand, inpaint, or remove elements via natural-language edits
- **Brand Kit** — Persist palette, font, logo, and tone — every generation respects the kit automatically
- **Templates Library** — Pre-built recipes for Instagram posts, story ads, LinkedIn banners, YouTube thumbnails, A4 posters, business cards, e-commerce hero shots, app icons, t-shirt prints, motion ads
- **Vectorize & Export** — Convert raster outputs to SVG, remove backgrounds cleanly, upscale to 4K print-ready
- **Workflow Studio** — Visual node-based editor to chain models into repeatable design pipelines (powered by [Vibe Workflow](https://github.com/SamurAIGPT/Vibe-Workflow))
- **Smart Controls** — Aspect ratio, resolution, quality, duration, and seed pickers that adapt per model
- **Generation History** — Browse, revisit, and download every past design (persisted locally in browser storage)
- **Responsive UI** — Modern dark/glass interface that works on desktop and mobile
- **API Key Management** — Keys stored in browser `localStorage`, never sent anywhere except Muapi

### 🤖 Design Agent — How it Works

Give the agent a brief like *"launch kit for a sustainable coffee brand called Pinecone — modern, earthy, monochrome with one accent, plus a 9:16 launch video"* and it will:

1. **Plan** — break the brief into a deliverable list (logo, wordmark, palette swatches, IG launch post, story ad, A4 poster, business card, packaging mockup, 9:16 launch video, motion logo)
2. **Route** — pick the right model per asset (Recraft v3 for the logo, Ideogram v3 for the typographic poster, Nano Banana 2 Edit for product placement, Flux Pro for the hero shot, Kling / Sora / Veo / Runway / Luma Ray2 for video)
3. **Execute** — generate in dependency order, threading the brand palette and reference images forward at each step
4. **Assemble** — hand back the full kit as downloadable assets, organized by category

You can interrupt at any step, swap a model, lock a result, fork the plan, or hand-edit any intermediate output and resume.

### 🎨 Design Studio — Three Modes

| Mode | Trigger | Models | Best for |
| :--- | :--- | :--- | :--- |
| **Generate** | Default (no image) | 50+ t2i models with text-rendering routing | New designs from a brief |
| **Edit** | Reference image uploaded | 55+ i2i / inpaint / outpaint models | Refining, recoloring, restyling existing assets |
| **Agent** | Chat thread | All of the above + video models, planned by the agent | Multi-asset campaigns, brand kits, full identity sets |

### Supported Use Cases

| Asset | Recommended Models | Notes |
| :--- | :--- | :--- |
| **Posters / Flyers** | Ideogram v3, Flux Pro Ultra, Nano Banana 2 | Crisp typographic output, A4/A3 ready |
| **Social Posts (IG / TikTok / X)** | Seedream 5, Flux Dev, Nano Banana 2 | 1:1 / 4:5 / 9:16 templates included |
| **Logos** | Recraft v3, Ideogram v3 | Pair with Vectorize for SVG export |
| **Brand Identity Boards** | Flux Pro, GPT-Image, Nano Banana 2 Edit | Multi-image reference for consistency |
| **UI Mockups & App Screens** | Flux Dev, GPT-Image, Recraft v3 | Galileo AI / Stitch / v0 / Magic Patterns alternative |
| **Product Mockups & Lifestyle** | Nano Banana 2 Edit, Flux Kontext Pro | Place product on staged backgrounds |
| **Illustrations** | Flux Dev, SDXL, Anything v5 | Stylized character & scene work |
| **YouTube Thumbnails** | Ideogram v3, Nano Banana 2 | Readable bold text + face composition |
| **Print (≥ 300 DPI)** | Flux Pro Ultra, Imagen 4 Ultra | Pair with Clarity / Magnific upscaler |
| **Packaging & Merch** | Recraft v3, Flux Pro | Vector + repeat-pattern friendly |
| **Motion Ads / Social Video** | Kling v3, Sora 2, Veo 3, Runway, Luma Ray2 | 9:16 / 1:1 / 16:9, 5–15s |
| **Animated Logos** | Kling I2V, Runway I2V, Luma Ray2 I2V | Animate static logo through i2v |
| **Spokesperson / Talking Head** | Infinite Talk, LTX 2.3 Lipsync, Wan 2.2 Speech-to-Video | Portrait + audio → video |

### 🔀 Workflow Studio

The **Workflow Studio** lets you build and run multi-step design pipelines without writing code.

**Key capabilities:**
- **Templates** — Start from pre-built design pipelines (logo + kit, social bundle, ad variants, product photoshoot, motion ad)
- **My Workflows** — Save and manage your own pipelines
- **Community** — Browse and run workflows published by other users
- **Node-based Builder** — Drag-and-drop visual editor connecting models and routing outputs between steps
- **Playground** — Run any workflow interactively with a form UI; results render inline
- **API execution** — Every workflow is also callable via the Muapi API

> 💡 **Want to add workflows to your own app?** Check out **[Vibe Workflow](https://github.com/SamurAIGPT/Vibe-Workflow)** — the open-source workflow engine powering this feature.

## 🚀 Quick Start

> Studio code is being added — for now this repo holds the agent design and roadmap. Watch / star the repo to be notified when the studio lands. The hosted version at [dev.muapi.ai/open-lovart](https://dev.muapi.ai/open-lovart) is live.

### Prerequisites (when self-hosting lands)

- [Node.js](https://nodejs.org/) (v18+)
- A [Muapi.ai](https://muapi.ai) API key (free tier available)

### Setup

```bash
# Clone the repository
git clone https://github.com/Anil-matcha/Open-Lovart.git
cd Open-Lovart

# Install dependencies
npm run setup

# Start the dev server
npm run dev
```

Visit `http://localhost:3000` and enter your Muapi API key on first launch.

### Production Build

```bash
npm run build
npm run start
```

## 🎨 Supported Model Categories

| Category | Count | Examples |
|---|---|---|
| **Text-to-Image (Design)** | 50+ | Flux 2 Pro, Nano Banana 2, Ideogram v3, Seedream 5, GPT-Image, Recraft v3, Midjourney v7, Imagen 4 Ultra |
| **Image-to-Image (Edit)** | 55+ | Nano Banana 2 Edit, Flux Kontext Pro/Max, GPT-Image Edit, Seededit v3, Seedream 5 Edit |
| **Vector / Logo** | 5+ | Recraft v3, Ideogram v3, Vectorizer.AI |
| **Background Removal** | 3+ | BiRefNet, RemBG, BG-Remover-v2 |
| **Upscaling (Print-grade)** | 8+ | Real-ESRGAN, Clarity Upscaler, Topaz, Magnific |
| **Inpaint / Outpaint** | 10+ | Flux Fill Pro, GPT-Image Inpaint, Seededit |
| **Text-to-Video** | 40+ | Kling v3, Sora 2, Veo 3, Wan 2.6, Seedance 2.0, Runway Gen-3, Luma Ray2 |
| **Image-to-Video** | 60+ | Kling v2.1 I2V, Veo3 I2V, Runway I2V, Luma Ray2 I2V, Seedance 2.0 I2V |
| **Lip Sync** | 9 | Infinite Talk, Wan 2.2 Speech-to-Video, LTX 2.3 Lipsync, Sync, LatentSync |

## 🛠️ Tech Stack

- **Next.js 14** — App Router, server components, fast dev server
- **React 18** — Studio UI components
- **Tailwind CSS v3** — Utility-first styling
- **npm workspaces** — Monorepo with shared `packages/studio` library
- **Muapi.ai** — AI model API gateway
- **Vibe Workflow** — Open-source node-based workflow engine

## 🤔 How is this different from Lovart, Runway Agent, Luma Labs Agent, Krea Agent?

**Open Lovart** is a community-driven, open-source alternative to closed AI design agents — same agentic creative loop, none of the lock-in.

| | Lovart / Runway / Luma / Krea Agents | Open Lovart |
| :--- | :--- | :--- |
| **Cost** | Subscription + credit packs | Free (open-source) |
| **Credit caps** | Hard monthly limits | Pay-as-you-go via your own Muapi key |
| **Model coverage** | Proprietary or single-vendor stack | 200+ open & commercial models, image *and* video |
| **Agent loop** | Closed, opaque | Fully inspectable and forkable |
| **Static + motion** | Usually one or the other per agent | Both, in one plan |
| **Text rendering** | Limited / single model | Routed across Ideogram v3, Flux Pro, Nano Banana 2, GPT-Image |
| **Multi-image reference** | Limited | Up to 14 images per request |
| **Brand kit** | Basic | Persistent palette / font / logo / tone conditioning |
| **Custom planners / tools** | No | Yes — bring your own planner, model, or post-step |
| **Self-hosting** | No | Yes |
| **Data privacy** | Cloud-based | Your data stays local |
| **Source code** | Closed | MIT licensed |

## 📄 License

MIT

## 🙏 Credits

Built with [Muapi.ai](https://muapi.ai) — the unified API for AI image and video generation models.

---
*Looking for a free, open-source Lovart alternative? Open Lovart is an open-source AI design agent — a Lovart, Runway Agent, Luma Labs Agent, Krea Agent, Pika Agent, Galileo AI, Magic Patterns replacement that you can self-host, customize, and extend.*

This project is an independent, experimental, and open-source initiative and is not affiliated with, endorsed by, or associated with Lovart, Runway, Luma Labs, Krea AI, Pika Labs, Galileo AI, Magic Patterns, or any of their respective companies, products, or services. Any references to third-party platforms, models, or technologies are made solely for interoperability, benchmarking, research, or educational purposes. All trademarks, logos, and brand names are the property of their respective owners. If any content in this repository creates confusion or raises concerns, please contact us and we will promptly review and address it.

## FAQ

### What is Open AI Design Agent?

**Open AI Design Agent** is a free, open-source AI design agent — alternative to **Lovart AI**, **Runway Agent**, **Luma Labs Agent**, **Krea Agent**. It turns natural-language briefs into full creative deliverables by orchestrating **200+ image and video models**.

### Key Features

| Feature | Description |
|---------|-------------|
| **Design Agent** | Describe a brand/campaign → agent plans, picks models, generates, assembles the kit |
| **200+ Models** | Flux 2 Pro, Nano Banana 2, Ideogram v3, Recraft v3, Midjourney v7, Kling, Sora, Veo, Runway, Luma Ray2 |
| **Brand Kit** | Persist palette, fonts, logo, tone — every generation respects the kit |
| **Multi-Image Reference** | Up to 14 images for style transfer, brand consistency, product placement |
| **Motion Studio** | Animated logos, video ads, social video cutdowns (9:16/1:1/16:9) |
| **Templates Library** | Instagram posts, YouTube thumbnails, A4 posters, business cards, packaging mockups |
| **Vectorize & Export** | Convert raster to SVG, remove backgrounds, upscale to 4K print-ready |
| **Workflow Studio** | Visual node-based editor to chain models into repeatable pipelines |

### How to Get Started

**Hosted (No Install):** https://muapi.ai/assistant — Run directly in browser

**Self-Hosted:**
```bash
git clone https://github.com/Anil-matcha/Open-AI-Design-Agent.git
cd Open-AI-Design-Agent && npm run setup && npm run dev
```

Visit `http://localhost:3000` and enter your Muapi API key.

### Supported Asset Types

| Asset | Recommended Models |
|-------|---------------------|
| **Posters/Flyers** | Ideogram v3, Flux Pro Ultra, Nano Banana 2 |
| **Logos** | Recraft v3, Ideogram v3 (+ Vectorize for SVG) |
| **Social Posts** | Seedream 5, Flux Dev, Nano Banana 2 |
| **Product Mockups** | Nano Banana 2 Edit, Flux Kontext Pro |
| **Motion Ads** | Kling v3, Sora 2, Veo 3, Runway, Luma Ray2 |
| **YouTube Thumbnails** | Ideogram v3, Nano Banana 2 |

### Why Open vs Lovart/Runway/Luma/Krea?

- **Free & open-source** — MIT-licensed, no subscription, no credit caps
- **Self-hosted** — your briefs and outputs stay on your machine
- **Inspectable agent loop** — every plan and model choice is visible and editable
- **Static + motion in one agent** — same brief produces poster, social, and video

### Help Resources

| Resource | Link |
|----------|------|
| **Hosted Studio** | https://muapi.ai/assistant |
| **Reddit Community** | https://reddit.com/r/muapi |
| **Discord** | https://discord.gg/s7KW4fsqXK |
| **Related Projects** | [Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI), [Vibe Workflow](https://github.com/SamurAIGPT/Vibe-Workflow) |

### License

MIT License - Open source and free to use.
