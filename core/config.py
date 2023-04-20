# _*_ coding: utf-8 _*_

"""
config file
"""

import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str

    # settings
    ENV_PRE: str = "EA"
    APP_NAME: str = "EasyApi"
    APP_DOMAIN: str = "http://127.0.0.1:8000"

    # settings from environment variables -- email
    MAIL_SERVER = os.environ.get(f"{ENV_PRE}_MAIL_SERVER")
    MAIL_PORT = os.environ.get(f"{ENV_PRE}_MAIL_PORT")
    MAIL_USERNAME = os.environ.get(f"{ENV_PRE}_MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get(f"{ENV_PRE}_MAIL_PASSWORD")
    MAIL_SENDER = (APP_NAME, MAIL_USERNAME)

    # settings from environment variables -- database
    REDIS_URI: str = os.environ.get(f"{ENV_PRE}_REDIS_URI")
    DATABASE_URI: str = os.environ.get(f"{ENV_PRE}_DATABASE_URI")

    class Config:
        case_sensitive = True


settings = Settings()
