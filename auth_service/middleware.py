"""Request middleware: token validation."""
from datetime import datetime, timezone


def is_valid(token: dict) -> bool:
    """Return True if *token* has not expired."""
    now = datetime.now(timezone.utc)
    return token["exp"] > now
