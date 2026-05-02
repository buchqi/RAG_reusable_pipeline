import os 
from dotenv import load_dotenv 

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
GENERATION_MODEL = os.getenv("GENERATION_MODEL")

if not GEMINI_API_KEY :
    raise ValueError("Missing GEMINI_API_KEY")
if not EMBEDDING_MODEL:
    raise ValueError("Missing EMBEDDING_MODEL")
if not GENERATION_MODEL :
    raise ValueError("Missing GENERATION_MODEL")


