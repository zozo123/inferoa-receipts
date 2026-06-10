"""Token issuance for the auth service."""
from datetime import datetime, timedelta, timezone

TOKEN_TTL = timedelta(hours=1)


def issue_token(user_id: str) -> dict:
    """Issue a short-lived access token for *user_id*."""
    now = datetime.now(timezone.utc)
    return {
        "sub": user_id,
        "iat": now,
        "exp": now + TOKEN_TTL,
    }
