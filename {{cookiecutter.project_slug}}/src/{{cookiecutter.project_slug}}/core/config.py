# config.py

from {{cookiecutter.project_slug}}.data.fake_db import users_db

# Setting for the API


class Settings:
    PROJECT_NAME: str = {{ cookiecutter.project_name }}
    DESCRIPTION: str = {{cookiecutter.project_description}}
    CONTACT: dict[str] = {"name": {{cookiecutter.author}}, "e-mail": {{cookiecutter.email}}}
    PROJECT_VERSION: str = "1.0"
    USERS_DB = users_db

    # Scopes for user authorization

    SCOPES = {
        "superuser": "User with rights to delete and administes database entries."
    }

    # Setting for token encoding (the secret key is Hex 32)
    SECRET_KEY = "536813181b97e9b63698643c2c8b4edc44b78ca41071a1c92bc9ebdbc09c32de"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 15


settings = Settings()
