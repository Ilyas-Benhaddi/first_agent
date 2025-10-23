"""
Time Zone Agent - A simple example agent built with Google's Gemini API
This agent can tell you the current time in different cities around the world.
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai
from first_agent.agent import get_current_time

# Load environment variables
load_dotenv()


def run_agent():
    """Run the time zone agent in an interactive loop."""

    # Initialize the Google Gemini client
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY not found in environment variables.")
        print("Please set it in your .env file or environment.")
        return

    genai.configure(api_key=api_key)
    
    # Create the model with function calling
    model = genai.GenerativeModel(
        'gemini-1.5-flash',
        tools=[get_current_time]
    )

    print("=" * 60)
    print("Time Zone Agent - Ask me about the current time anywhere!")
    print("=" * 60)
    print("Available cities: New York, London, Tokyo, Paris, Sydney,")
    print("                  Dubai, Singapore, Los Angeles, Chicago, Toronto")
    print("\nType 'quit' or 'exit' to end the conversation.")
    print("=" * 60)
    print()

    # Start a chat session
    chat = model.start_chat(enable_automatic_function_calling=True)

    while True:
        # Get user input
        user_input = input("You: ").strip()

        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        try:
            # Send message and get response
            response = chat.send_message(user_input)
            print(f"\nAgent: {response.text}\n")
            
        except Exception as e:
            print(f"\nError: {e}\n")


if __name__ == "__main__":
    run_agent()
