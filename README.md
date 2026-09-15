# AI Gateway Test

A simple Python project demonstrating how to connect an application to a local **FreeLLMAPI** gateway using the **OpenAI-compatible API**.

The purpose of this project is to learn and experiment with multi-provider AI access through a single local API endpoint.

## Architecture

```text
Python Application
       |
       v
OpenAI Python SDK
       |
       v
FreeLLMAPI
http://localhost:3001/v1
       |
       +------------------+
       |                  |
       v                  v
   Google AI Studio      Groq
       |                  |
    Gemini          GPT-OSS 120B
```

## What This Project Demonstrates

- Using the OpenAI Python SDK with a non-OpenAI endpoint
- Connecting Python to a local AI gateway
- Using environment variables for API credentials
- Routing requests through FreeLLMAPI
- Using `auto` model selection
- Working with multiple AI providers through one API
- Keeping API credentials out of Git

## Prerequisites

- Python 3.10+
- FreeLLMAPI running locally
- At least one configured AI provider in FreeLLMAPI
- A FreeLLMAPI Unified API key

The default FreeLLMAPI endpoint used by this project is:

```text
http://localhost:3001/v1
```

## Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd ai-gateway-test
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file:

```text
FREELLMAPI_API_KEY=your-unified-api-key
FREELLMAPI_BASE_URL=http://localhost:3001/v1
```

**Never commit `.env` to GitHub.**

The repository's `.gitignore` already excludes it.

## Run

Make sure FreeLLMAPI is running and then execute:

```powershell
python main.py
```

The application sends a request using:

```text
model = auto
```

FreeLLMAPI then selects the appropriate model according to its active routing configuration.

## Example

The program prints:

```text
--- AI Response ---
<AI-generated response>

--- Routing ---
Model: openai/gpt-oss-120b
```

The selected provider/model may change depending on the FreeLLMAPI routing configuration and available providers.

## Routing Experiments

FreeLLMAPI supports different routing strategies.

Examples explored during development:

| Strategy | Example result |
|---|---|
| Fastest | Groq / GPT-OSS 120B |
| Balanced | Groq / GPT-OSS 120B |
| Smartest | Google / Gemini 3.6 Flash |

FreeLLMAPI also provides API-level model selectors such as:

```text
auto
auto:fast
auto:smart
auto:balanced
auto:reliable
```

These allow applications to request different routing behavior without changing provider-specific application code.

## Security

This project intentionally keeps credentials outside the source code.

Ignored files include:

```text
.env
.venv/
__pycache__/
*.pyc
```

Never commit API keys, passwords, tokens, or other secrets.

## Why Use an AI Gateway?

Instead of writing provider-specific code:

```text
Application
   |
   +--> Google API
   |
   +--> Groq API
   |
   +--> OpenAI API
   |
   +--> Other providers
```

the application can use one interface:

```text
Application
     |
     v
FreeLLMAPI
     |
     +--> Google
     +--> Groq
     +--> Other providers
```

This makes it easier to experiment with models, providers, routing strategies, and failover without changing the core application.

## Learning Goals

This project is part of an ongoing AI engineering learning path.

Future experiments may include:

- Multi-provider AI applications
- RAG applications

## Disclaimer

This project is intended for **learning, experimentation, and prototyping**.

AI provider availability, limits, pricing, models, and free-tier policies may change. Always follow the terms and usage policies of the providers you use.
