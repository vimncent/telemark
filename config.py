import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")
OFFLOAD_PROBABILITY = float(os.getenv("OFFLOAD_PROBABILITY", "0.01"))
SOFT_LIMIT_ROWS = int(os.getenv("SOFT_LIMIT_ROWS", "200000"))
DATABASE_URL = os.getenv("DATABASE_URL")
