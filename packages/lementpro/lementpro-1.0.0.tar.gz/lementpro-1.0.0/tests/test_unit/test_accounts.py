from unittest.mock import patch, MagicMock
from lementpro.services.accounts import Accounts


def test_refresh_token(login):
    mock_token = MagicMock()
    mock_token.json.return_value = {"accessToken": "test_token", "refreshToken": "test", "expiredIn": 1685699669}
    mock_token.status_code.return_value = 200
    mock_refresh_token = MagicMock(return_value=mock_token)
    with patch("lementpro.services.accounts.Accounts.refresh_token", mock_refresh_token):
        response = Accounts().refresh_token(login, refreshToken="test_refresh")
        assert response.status_code() == 200
        assert response.json()["accessToken"] == "test_token"
