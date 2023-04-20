import os
from dotenv import load_dotenv
from pydantic import BaseSettings, SecretStr

load_dotenv()


class TG_BOT_SETTINGS(BaseSettings):
	tg_api: SecretStr = os.getenv('TOKEN_TG', None)
