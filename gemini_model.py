import os 
from agents import (
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    RunConfig
)
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_URL", "https://generativelanguage.googleapis.com/v1beta/openai/")

if not gemini_api_key or not gemini_base_url:
    raise ValueError("API_KEY and BASE_URL must be set in the environment variables.") # Ensure these are set in your .env file
 
# setting up the OpenAI client with Gemini API key and base URL
client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = gemini_base_url,
)

# model 
geminiModel = OpenAIChatCompletionsModel(
    openai_client = client,
    model = "gemini-2.0-flash",
)

# configuring the model
config = RunConfig(
    model = geminiModel,
    model_provider = client,
    tracing_disabled=True
)

