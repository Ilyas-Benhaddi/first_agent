"""
Time Zone Agent - A simple example agent built with Anthropic's SDK
This agent can tell you the current time in different cities around the world.
It demonstrates how to:
- Define tools for the agent to use
- Handle tool calls in a conversation loop
- Process user queries with AI assistance
"""

import os
from dotenv import load_dotenv
from anthropic import Anthropic
from first_agent.agent import TOOLS, process_tool_call

# Load environment variables
load_dotenv()


def run_agent():
    """Run the time zone agent in an interactive loop."""

    # Initialize the Anthropic client
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found in environment variables.")
        print("Please set it in your .env file or environment.")
        return

    client = Anthropic(api_key=api_key)

    print("=" * 60)
    print("Time Zone Agent - Ask me about the current time anywhere!")
    print("=" * 60)
    print("Available cities: New York, London, Tokyo, Paris, Sydney,")
    print("                  Dubai, Singapore, Los Angeles, Chicago, Toronto")
    print("\nType 'quit' or 'exit' to end the conversation.")
    print("=" * 60)
    print()

    # Conversation history
    messages = []

    while True:
        # Get user input
        user_input = input("You: ").strip()

        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        # Add user message to history
        messages.append({
            "role": "user",
            "content": user_input
        })

        # Initial API call
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            tools=TOOLS,
            messages=messages
        )

        # Process the response and handle tool calls
        while response.stop_reason == "tool_use":
            # Add assistant's response to messages
            messages.append({
                "role": "assistant",
                "content": response.content
            })

            # Process all tool calls
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    tool_name = block.name
                    tool_input = block.input

                    print(f"\n[Agent is using tool: {tool_name}]")

                    # Execute the tool
                    result = process_tool_call(tool_name, tool_input)

                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": str(result)
                    })

            # Add tool results to messages
            messages.append({
                "role": "user",
                "content": tool_results
            })

            # Get next response
            response = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                tools=TOOLS,
                messages=messages
            )

        # Add final assistant response to messages
        messages.append({
            "role": "assistant",
            "content": response.content
        })

        # Extract and print the text response
        for block in response.content:
            if hasattr(block, "text"):
                print(f"\nAgent: {block.text}")

        print()


if __name__ == "__main__":
    run_agent()