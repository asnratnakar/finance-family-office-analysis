import os

import keyring


SERVICE_NAME = "personal-finance-family-office"


def get_secret(name: str) -> str | None:
    """Return a secret from OS keyring or environment, without logging it."""
    env_name = name.upper()
    env_value = os.getenv(env_name)
    if env_value:
        return env_value
    return keyring.get_password(SERVICE_NAME, name)


def set_secret(name: str, value: str) -> None:
    """Store a secret in OS keyring; never persist it in repository files."""
    keyring.set_password(SERVICE_NAME, name, value)
