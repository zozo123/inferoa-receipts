from auth_service.middleware import is_valid
from auth_service.token import issue_token


def test_token_refresh():
    token = issue_token("user-1")
    assert is_valid(token), "freshly issued token must be valid"


def test_expired_token_rejected():
    from datetime import datetime, timedelta, timezone

    token = {
        "sub": "user-1",
        "iat": datetime.now(timezone.utc) - timedelta(hours=2),
        "exp": datetime.now(timezone.utc) - timedelta(hours=1),
    }
    assert not is_valid(token), "expired token must be rejected"
