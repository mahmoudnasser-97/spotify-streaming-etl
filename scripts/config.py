import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
USER_ID = os.getenv("SPOTIFY_USER_ID")

DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"

SPOTIFY_TOKEN = os.getenv("SPOTIFY_TOKEN")