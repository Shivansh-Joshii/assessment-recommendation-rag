from pathlib import Path
from dotenv import load_dotenv
import os

# Load .env file
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

# API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Groq Model
MODEL_NAME = "llama-3.3-70b-versatile"

# Validate API Key
if GROQ_API_KEY is None:
    raise ValueError("GROQ_API_KEY not found. Please check your .env file.")