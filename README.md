# AI Gateway

A Python project demonstrating how applications can connect to multiple AI providers through a single **OpenAI-compatible AI gateway**.

This project uses **FreeLLMAPI** as the local gateway and connects providers such as Google AI Studio and Groq behind one unified API interface.

## Architecture

```text
                    AI Applications
                          |
                          v
                 OpenAI Python SDK
                          |
                          v
                  ┌──────────────┐
                  │  AI Gateway  │
                  │  localhost   │
                  │   :3001/v1   │
                  └──────┬───────┘
                         |
               ┌─────────┴─────────┐
               |                   |
               v                   v
        Google AI Studio          Groq
               |                   |
            Gemini            GPT-OSS 120B
```

## Project Goals

The goal of this project is to learn how a single AI gateway can provide a consistent API interface while routing requests to different AI providers and models.

The project is designed as a foundation for future AI applications and experiments.

## What This Project Demonstrates

- OpenAI-compatible API usage
- Python integration with an AI gateway
- Multi-provider AI access
- AI model routing
- Automatic model selection
- Fastest, Balanced, and Smartest routing strategies
- Environment-based API configuration
- Secure handling of API credentials
- Provider abstraction
- A reusable foundation for future AI applications

## Current AI Providers

### Google AI Studio

Configured models include Gemini models such as:

- Gemini 3.6 Flash
- Gemini 3.5 Flash
- Gemini 3 Flash Preview
- Gemini 3.5 Flash Lite
- Gemini 3.1 Flash-Lite
- Gemini 2.5 Flash
- Gemini 2.5 Flash-Lite
- Gemma models

### Groq

Configured models include:

- GPT-OSS 120B
- GPT-OSS 20B
- Compound
- Compound Mini
- Other available Groq models

Provider availability and model availability may change over time.

## API Architecture

Applications communicate with one local endpoint:

```text
http://localhost:3001/v1
```

Instead of implementing separate integrations:

```text
Application
   |
   +--> Google API
   +--> Groq API
   +--> OpenAI API
   +--> Other providers
```

the application communicates with the gateway:

```text
Application
      |
      v
  AI Gateway
      |
      +--> Google
      +--> Groq
      +--> Other providers
```

This allows the application code to remain largely provider-independent.

## Routing

The gateway supports different routing strategies.

### Fastest

Prioritizes model speed.

Example observed result:

```text
Groq → GPT-OSS 120B
```

### Balanced

Balances:

- Reliability
- Speed
- Intelligence

Example observed result:

```text
Groq → GPT-OSS 120B
```

### Smartest

Places greater weight on model intelligence.

Example observed result:

```text
Google → Gemini 3.6 Flash
```

## API-Level Model Selection

The gateway can also accept routing selectors such as:

```text
auto
auto:fast
auto:smart
auto:balanced
auto:reliable
```

For example:

```python
response = client.chat.completions.create(
    model="auto:fast",
    messages=[
        {
            "role": "user",
            "content": "Explain RAG in simple terms.",
        }
    ],
)
```

The application does not need to know which provider ultimately handles the request.

## Python Client

This project uses the standard OpenAI Python SDK.

Example:

```python
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("FREELLMAPI_API_KEY"),
    base_url=os.getenv("FREELLMAPI_BASE_URL"),
)

response = client.chat.completions.create(
    model="auto",
    messages=[
        {
            "role": "user",
            "content": "Explain what an AI API gateway is in simple terms.",
        }
    ],
)

print(response.choices[0].message.content)
print(response.model)
```

## Setup

### Prerequisites

- Python 3.10+
- Git
- FreeLLMAPI running locally
- At least one configured AI provider
- FreeLLMAPI Unified API key

### Clone

```bash
git clone https://github.com/sivasreeonline/ai-gateway.git
cd ai-gateway
```

### Create a virtual environment

```powershell
python -m venv .venv
```

### Activate the environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install dependencies

```powershell
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file:

```text
FREELLMAPI_API_KEY=your-unified-api-key
FREELLMAPI_BASE_URL=http://localhost:3001/v1
```

Never commit `.env` to GitHub.

The repository's `.gitignore` already excludes it.

### Run

Make sure FreeLLMAPI is running and execute:

```powershell
python main.py
```

Example output:

```text
--- AI Response ---
<AI-generated response>

--- Routing ---
Model: openai/gpt-oss-120b
```

The selected provider and model can change depending on the active routing strategy and available models.

## Security

API credentials are stored outside the source code.

The following files are excluded from Git:

```text
.env
.venv/
__pycache__/
*.pyc
```

Never commit:

- API keys
- Passwords
- Access tokens
- Secret credentials
- Private configuration files



## Disclaimer

This project is intended for **learning, experimentation, and prototyping**.

AI provider availability, pricing, quotas, models, and free-tier policies may change. Always follow the terms and usage policies of the providers you use.
