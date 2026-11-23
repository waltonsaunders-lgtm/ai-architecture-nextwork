 
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load our private API key
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
    http_options=types.HttpOptions(
        timeout=15000,
        retry_options=types.HttpRetryOptions(
            attempts=1
        )
    )
)

# Send our first AI request
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Reply with exactly: Gemini connection successful!"
)

print(response.text)
