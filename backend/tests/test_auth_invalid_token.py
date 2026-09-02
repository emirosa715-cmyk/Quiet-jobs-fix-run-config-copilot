import requests


def test_me_with_invalid_token_returns_401():
    resp = requests.get(
        "http://localhost:8000/api/auth/me",
        headers={"Authorization": "Bearer garbage"},
        timeout=5,
    )
    assert resp.status_code == 401
