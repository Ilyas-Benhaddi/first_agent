from datetime import datetime
import pytz
from typing import Any

def get_current_time(city: str) -> dict:
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


# Tool schema for Anthropic API
TOOLS = [
    {
        "name": "get_current_time",
        "description": "Get the current time in a specific city. Useful when users ask about the current time in different locations around the world.",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The name of the city to get the time for (e.g., 'New York', 'London', 'Tokyo')"
                }
            },
            "required": ["city"]
        }
    }
]


def process_tool_call(tool_name: str, tool_input: dict[str, Any]) -> Any:
    """Process a tool call and return the result.
    Args:
        tool_name: The name of the tool to call
        tool_input: The input parameters for the tool
    Returns:
        The result of the tool execution
    """
    if tool_name == "get_current_time":
        return get_current_time(**tool_input)
    else:
        return {"status": "error", "message": f"Unknown tool: {tool_name}"}