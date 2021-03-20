# settings.py
from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only
import os
load_dotenv()


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

SERVER_IP = str(os.getenv("SERVER_IP"))
SERVER_PORT = int(os.getenv("SERVER_PORT"))