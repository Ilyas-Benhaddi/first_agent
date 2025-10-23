"""
Time Zone Agent using Google ADK
"""

from datetime import datetime
import pytz
from google.adk import Agent


def get_current_time(city: str) -> str:
    """Returns the current time in a specified city.
    
    Args:
        city: The name of the city to get the time for (e.g., 'New York', 'London', 'Tokyo')
    
    Returns:
        A string with the current time or error message
    """
    # Timezone mapping
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
        return f"The current time in {city} is {current_time} ({timezone_name})"
    else:
        available_cities = ", ".join([c.title() for c in city_timezones.keys()])
        return f"City '{city}' not found. Available cities: {available_cities}"


# Create the ADK agent with correct parameters
root_agent = Agent(
    name="TimeZoneAgent",
    model="gemini-1.5-flash",
    instruction="""You are a helpful time zone assistant. You can tell users the current time in different cities around the world.

Available cities: New York, London, Tokyo, Paris, Sydney, Dubai, Singapore, Los Angeles, Chicago, Toronto.

When a user asks about the time in a city, use the get_current_time function to fetch the current time.""",
    tools=[get_current_time]
)