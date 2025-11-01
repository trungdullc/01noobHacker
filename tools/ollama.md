# ollama
```
Description: Language Learning Model (LLM)
Source: https://ollama.com/

Info: Ollama is a tool that lets you run AI language learning models locally on your own computer — without needing the cloud

# Download and Install

# look at help
$ ollama

# Download LLM from https://ollama.com/library
granite3.3
IBM Granite 2B and 8B models are 128K context length language models that have been fine-tuned for improved reasoning and instruction-following capabilities.

tools       2b      8b

$ ollama pull granite3.3

# Run LLM locally
$ ollama granite3.3 "hi"

# DL uv: An extremely fast Python package and project manager, written in Rust.
# Source: https://github.com/astral-sh/uv
$ pip install uv                        $ brew install uv

# Test
# uvx → runs a Python-based CLI package without installing it permanently
# chuk-llm → is a helper tool that interacts with different LLM backends
# test ollama → tells chuk-llm to check if Ollama is available
$ uvx chuk-llm test ollama

$ uvx chuk-llm ask_granite "hi"

# Create new python project
$ uv init myproject
$ code .

# Test default main()
$ uv run main.py

# Install chuck-llm package into python project
$ uv add chuk-llm

# Import ollama granite3.3 into project and edit main.py
from chuk_llm import ask_ollama_granite

print(ask_ollama_granite("hi"))

# Run
$ uv run main.py
```

## main.py 2nd edit
```python
import asyncio
from chuk_llm import ask_ollama_granite, stream_ollama_granite

async def stream_example():
    """
    Streams a response from the Granite LLM and prints it in real-time.

    The function sends the prompt "Who is Hacker X" to the Granite model
    and asynchronously prints each chunk of the model's response as it is generated.
    """
    async for chunk in stream_ollama_granite("Who is Hacker X"):
        print(chunk, end="", flush=True)

if __name__ == "__main__":
    # Run the async streaming example
    asyncio.run(stream_example())

# Run
$ uv run main.py
```

## main.py 3rd edit, can be pirate, reviewer, AI Agent
```python
import asyncio
from chuk_llm import ask_ollama_granite, stream_ollama_granite

async def stream_example():
    persona = "You are a pirate name Rogers, and always responds back in pirate"

    async for chunk in stream_ollama_granite("Who is Hacker X",system_prompt = persona):
        print(chunk, end="", flush=True)

if __name__ == "__main__":
    asyncio.run(stream_example())

# Run
$ uv run main.py
```

## main.py 4th edit, conversation mode
```python
import asyncio
from chuk_llm import ask_ollama_granite, stream_ollama_granite, conversation

async def stream_example():
    async with conversation(provider="ollama", model="granite3.3") as chat:
        question = "My name is Hacker and i am learning python"
        print("Input: " + question)

        response = await chat.ask(question)
        print(response)

        followup = "What am I learning"
        print("Input: " + followup)
        response = await chat.ask(followup)
        print(response)

if __name__ == "__main__":
    asyncio.run(stream_example())

# Run
$ uv run main.py
```

## main.py 5th edit, low lvl libraries
```python
import asyncio
from chuk_llm import get_client

async def stream_example():
    async with conversation(provider="ollama", model="granite3.3") as chat:
        

if __name__ == "__main__":
    asyncio.run(stream_example())
        client = get_client(provider="ollama", model="granite3.3:latest)

        messages = [
            {"role": "system", "content": "You are a pirate name Rogers, and always responds back in pirate" },
            {"role": "user", "content": "Hi"}
        ]

        completion = await client.create_completion(messages=messages)
        print(completion["response"])

# Run
$ uv run main.py
```

## Side Quest
```python
"""
Example: Talk to Ollama Granite3.3 model directly using requests
"""

import requests

# Define Ollama API endpoint
OLLAMA_API_URL = "http://localhost:11434/api/generate"

# Define system persona and user message
messages = [
    {
        "role": "system",
        "content": "You are a pirate named Rogers, and always respond back in pirate-speak."
    },
    {
        "role": "user",
        "content": "Hi"
    }
]

# Prepare request payload
payload = {
    "model": "granite3.3",  # model name
    "messages": messages
}

# Send POST request to Ollama API
response = requests.post(OLLAMA_API_URL, json=payload)

# Check if request was successful
if response.status_code == 200:
    data = response.json()
    print("Ollama response:\n")
    print(data.get("response"))
else:
    print(f"Error: {response.status_code}")
    print(response.text)

```

## Back to README.md
[BACK](../README.md)