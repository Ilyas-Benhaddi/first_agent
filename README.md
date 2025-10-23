# Time Zone Agent

A simple example agent built with Google's Agent Development Kit (ADK) that demonstrates how to create an AI agent with custom tools. This agent can tell you the current time in different cities around the world.

## What This Example Teaches

This project demonstrates the core concepts of building an agent with Google's ADK and Gemini:

1. **Tool Definition**: How to define tools (functions) that the AI can use
2. **Tool Schema**: How to structure tool descriptions so the AI knows when and how to use them
3. **Conversation Loop**: How to manage a back-and-forth conversation with tool usage
4. **Tool Execution**: How to execute tools and return results to the AI
5. **Project Structure**: How to organize a simple agent project

## Features

- Interactive CLI chat interface
- Real-time timezone conversion
- Support for 10 major cities worldwide
- Clean conversation loop with tool usage

## Supported Cities

- New York
- London
- Tokyo
- Paris
- Sydney
- Dubai
- Singapore
- Los Angeles
- Chicago
- Toronto

## Prerequisites

- Python 3.8 or higher
- A Google API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
- Google Agent Development Kit (ADK)

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd first_agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
pip install google-adk
```

3. Set up your API key:

Create a `.env` file in the project root:
```bash
GOOGLE_API_KEY="your_google_api_key_here"
GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

Or copy the example file and edit it:
```bash
cp .env.example .env
# Then edit .env with your actual API key
```

## Usage

Run the agent using ADK:
```bash
adk run first_agent
```

Example conversation:
```
You: What time is it in Tokyo?
Agent: The current time in Tokyo is 3:45 PM (Asia/Tokyo timezone).
You: How about London and New York?
Agent: Let me check both cities for you...
The current time in London is 6:45 AM (Europe/London timezone).
The current time in New York is 1:45 AM (America/New_York timezone).
You: quit
Goodbye!
```

## Project Structure

```
first_agent/
├── first_agent/
│   ├── __init__.py          # Package initialization
│   └── agent.py             # Tool definitions and tool execution logic
├── main.py                  # Main agent entry point with conversation loop
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (API keys)
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## How It Works

### 1. Tool Definition (agent.py)

The agent has access to one tool: `get_current_time`. The tool is defined with:
- A clear description for the AI
- An input schema (what parameters it accepts)
- Implementation logic (the actual Python function)

### 2. Tool Schema

```python
TOOLS = [
    {
        "name": "get_current_time",
        "description": "Get the current time in a specific city...",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The name of the city..."
                }
            },
            "required": ["city"]
        }
    }
]
```

### 3. Conversation Loop (main.py)

The agent follows this flow:
1. User sends a message
2. AI decides if it needs to use a tool
3. If yes, tool is executed and result is sent back to AI
4. AI formulates a response with the tool results
5. Response is shown to user

## Extending This Example

You can extend this agent by:

1. **Adding More Cities**: Edit the `city_timezones` dictionary in `agent.py`

2. **Adding New Tools**: Create new functions and add them to the `TOOLS` list
   - Example: Weather lookup, currency conversion, etc.

3. **Adding Persistence**: Store conversation history to a database

4. **Adding a Web Interface**: Replace the CLI with Flask/FastAPI

5. **Better Error Handling**: Add try-except blocks and validation

## Key Concepts Explained

### What is a Tool?

A tool is a function that the AI can call to get information or perform actions. The AI doesn't execute the function directly - it tells YOU it wants to use the tool, you execute it, and return the result.

### Why the Loop?

The conversation loop handles the back-and-forth:
- AI might need to call multiple tools
- AI needs to see tool results before responding
- This creates the "agentic" behavior

### Tool Use Flow

```
User: "What time is it in Tokyo?"
  ↓
AI: "I'll use get_current_time tool with city='Tokyo'"
  ↓
Your code: Executes get_current_time("Tokyo")
  ↓
Your code: Returns {"status": "success", "time": "3:45 PM"}
  ↓
AI: "The current time in Tokyo is 3:45 PM"
  ↓
User sees response
```

## Troubleshooting

**"GOOGLE_API_KEY not found"**
- Make sure your `.env` file exists in the project root (not in `first_agent/` subdirectory)
- Verify the .env file contains both `GOOGLE_API_KEY` and `GOOGLE_GENAI_USE_VERTEXAI=FALSE`
- Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

**"Model not found" or 404 errors**
- Make sure you have `GOOGLE_GENAI_USE_VERTEXAI=FALSE` in your .env file
- This tells ADK to use Google AI Studio instead of Vertex AI
- Verify your model name is `gemini-1.5-flash-002` in `first_agent/agent.py`

**"Module not found"**
- Run `pip install -r requirements.txt`
- Run `pip install google-adk`
- Make sure you're in the project directory

**"City not found"**
- Check the list of supported cities
- City names are case-insensitive

## Learning Resources

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)
- [Google AI Studio](https://aistudio.google.com/)

## License

This is an example project for learning purposes. Feel free to modify and use it as you like.