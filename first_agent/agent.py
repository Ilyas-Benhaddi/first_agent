from datetime import datetime
import pytz

def get_current_time(city: str) -> dict:
    """Returns the actual current time in a specified city."""
    # Simple timezone mapping (you can expand this)
    city_timezones = {
        "new york": "America/New_York",
        "london": "Europe/London",
        "tokyo": "Asia/Tokyo",
        "paris": "Europe/Paris",
        # Add more cities as needed
    }
    
    city_lower = city.lower()
    if city_lower in city_timezones:
        tz = pytz.timezone(city_timezones[city_lower])
        current_time = datetime.now(tz).strftime("%I:%M %p")
        return {"status": "success", "city": city, "time": current_time}
    else:
        return {"status": "error", "city": city, "message": "City not found"}