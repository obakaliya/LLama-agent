# LLama-Agent

LLama-Agent is an AI-powered assistant that leverages a large language model and DuckDuckGo to provide intelligent, context-aware responses. It retains context from past interactions and always includes sources in its answers.

## Installation

1. Clone the repository and navigate to its directory.

2. Create and activate a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -U phidata
   pip install -U phidata openai duckduckgo-search
   pip install groq
   ```

4. Set up the environment file:
   ```bash
   cp .env.example .env
   ```

5. Get your API key from [Groq Console](https://groqconsole.groq.com) and add it to the `.env` file under `GROQ_API_KEY`.

## Features

- **AI-Powered**: Uses the `llama-3.3-70b-versatile` model for intelligent and versatile responses.
- **Web Search Integration**: Powered by DuckDuckGo for real-time information retrieval.
- **Context Awareness**: Maintains memory of past interactions for improved answers.
- **Credible Responses**: Always includes sources to ensure trustworthiness.

## Usage

After completing the setup, run the agent script to start an interactive session. Type your queries, and the agent will respond with accurate answers and sources.
