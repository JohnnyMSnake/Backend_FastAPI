import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

settings = Settings()

# Posibles rutas a manejar uwu
ORIGINS = [
    "http://localhost:3000",  # frontend en el localhost
]