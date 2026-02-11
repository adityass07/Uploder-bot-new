# DON'T add anything here just add in render's secret or env section 
from os import environ

API_ID = int(environ.get("API_ID", "30929822"))
API_HASH = environ.get("API_HASH", "8586e9580c6480b65d23150cec959506")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

