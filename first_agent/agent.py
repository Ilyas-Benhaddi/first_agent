from datetime import datetime
import pytz
from google.adk import Agent
from google.adk.tools import AnthropicTool


def get_current_time_impl(city: str) -> dict:
    """Returns the actual current time in a specified city.
    Args:
        city: The name of the city to get the time for (e.g., 'New York', 'London', 'Tokyo')
    Returns:
        A dictionary with status, city name, and current time or error message
    """
    # Simple timezone mapping (you can expand this)
    city_timezones = {
        "new york": "America/New_York",
        "london": "Europe/London",
        "tokyo": "Asia/Tokyo",
        "paris": "Europe/Paris",
        "sydney": "Australia/Sydney",
        "dubai": "Asia/Dubai",
        "singapore": "Asia/Singapore",
        "los angeles": "America/Los_Angeles",
        "chicago": "America/Chicago",
        "toronto": "America/Toronto",
    }

    city_lower = city.lower()
    if city_lower in city_timezones:
        tz = pytz.timezone(city_timezones[city_lower])
        current_time = datetime.now(tz).strftime("%I:%M %p")
        timezone_name = city_timezones[city_lower]
        return {
            "status": "success",
            "city": city,
            "time": current_time,
            "timezone": timezone_name
        }
    else:
        available_cities = ", ".join([c.title() for c in city_timezones.keys()])
        return {
            "status": "error",
            "city": city,
            "message": f"City not found. Available cities: {available_cities}"
        }


# Define the tool for ADK
get_current_time_tool = AnthropicTool(
    name="get_current_time",
    description="Get the current time in a specific city. Useful when users ask about the current time in different locations around the world.",
    input_schema={
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The name of the city to get the time for (e.g., 'New York', 'London', 'Tokyo')"
            }
        },
        "required": ["city"]
    },
    function=get_current_time_impl
)


# Create the ADK agent
root_agent = Agent(
    name="TimeZoneAgent",
    model="claude-3-5-sonnet-20241022",
    system_prompt="""You are a helpful time zone assistant. You can tell users the current time in different cities around the world.

Available cities: New York, London, Tokyo, Paris, Sydney, Dubai, Singapore, Los Angeles, Chicago, Toronto.

When a user asks about the time in a city, use the get_current_time tool to fetch the current time.""",
    tools=[get_current_time_tool]
)