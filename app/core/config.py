import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///C:/Users/maksi/Desktop/soccer_hub/instance/soccer_hub.db")

settings = Settings()
