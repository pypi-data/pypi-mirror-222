import pytest
from unittest.mock import patch, MagicMock
from lementpro.data.user import User
from lementpro.data.accesstokenmodel import AccessTokenModel
from lementpro.services.accounts import Accounts


@pytest.fixture
def login():
    mock_token = MagicMock()
    mock_token.json.return_value = {"accessToken": "test_token"}
    mock_login = MagicMock(return_value=mock_token)
    user = User(root_url="https://ugate.dev.lement.ru", specific_headers={"X-Lement-Host": "lementtest.dev.lement.ru"})
    with patch("lementpro.services.accounts.Accounts.login", mock_login):
        access_token = AccessTokenModel(
            **Accounts().login(login="dmoz", password="qwe", by_user=user).json()
        ).accessToken
    user.access_token = access_token
    yield user
