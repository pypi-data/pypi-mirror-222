from unittest.mock import patch, MagicMock
from lementpro.services.users import Users


def test_user(login):
    data = {
        "data": [
            {
                "id": 104125,
                "userName": "333@333.ru",
                "companyId": 1,
                "email": "333@333.ru",
                "firstName": "222",
                "isDismissed": False,
                "isDisabled": False,
                "isSystem": False,
                "position": "",
                "role": "employee",
                "departmentId": 1,
                "displayName": "222",
                "extension": {"systemTheme": "light", "startupPage": "/", "showSystemFoldersObjectsCount": False},
            },
            {
                "id": 104124,
                "userName": "1@1.ru",
                "companyId": 1,
                "email": "1@1.ru",
                "firstName": "123 123 123",
                "isDismissed": False,
                "isDisabled": False,
                "isSystem": False,
                "position": "",
                "role": "employee",
                "departmentId": 1,
                "displayName": "123 123 123",
                "extension": {
                    "avatarFileId": 567007,
                    "systemTheme": "light",
                    "startupPage": "/",
                    "showSystemFoldersObjectsCount": False,
                },
            },
        ]
    }
    mock_users = MagicMock()
    mock_users.json.return_value = data
    mock_users.status_code.return_value = 200
    mock_get_users = MagicMock(return_value=mock_users)
    with patch("lementpro.services.users.Users.users", mock_get_users):
        response = Users().users(by_user=login)
        assert response.json()["data"][1]["email"] == "1@1.ru"
        assert response.status_code() == 200


def test_post_mailbox(login):
    data = {"id": "registred_mailbox"}
    mock_mail = MagicMock()
    mock_mail.json.return_value = data
    mock_mail.status_code.return_value = 200
    mock_post_mail = MagicMock(return_value=mock_mail)
    with patch("lementpro.services.users.Users.post_mailbox", mock_post_mail):
        response = Users().post_mailbox(
            by_user=login, login="test_mail", password="123", smtpHost="smtp.mail.ru", smtpPort=465
        )
        assert response.status_code() == 200
        assert response.json()["id"] == "registred_mailbox"


def test_patch_mailbox(login):
    mock_mail = MagicMock()
    mock_mail.status_code.return_value = 204
    mock_patch_mail = MagicMock(return_value=mock_mail)
    with patch("lementpro.services.users.Users.patch_mailbox", mock_patch_mail):
        response = Users().patch_mailbox(by_user=login)
        assert response.status_code() == 204
    mock_fail = MagicMock()
    mock_fail.status_code.return_value = 401
    mock_patch_fail = MagicMock(return_value=mock_fail)
    with patch("lementpro.services.users.Users.patch_mailbox", mock_patch_fail):
        response = Users().patch_mailbox(by_user=None)
        assert response.status_code() == 401


def test_get_mailbox(login):
    data = {
        "id": 123,
        "companyId": 1,
        "userId": 24,
        "login": "test_mail",
        "smtpHost": "smtp.mail.ru",
        "smtpPort": 465,
        "imapHost": "imap.mail.ru",
        "imapPort": 100,
        "isDisabled": False,
        "signature": "string",
        "passwordHash": "string",
    }
    mock_mail = MagicMock()
    mock_mail.json.return_value = data
    mock_mail.status_code.return_value = 200
    mock_get_mail = MagicMock(return_value=mock_mail)
    with patch("lementpro.services.users.Users.get_mailbox", mock_get_mail):
        response = Users().get_mailbox(by_user=login)
        assert response.status_code() == 200
        assert response.json()["id"] == 123
        assert response.json()["login"] == "test_mail"


def test_delete_mailbox(login):
    mock_mail = MagicMock()
    mock_mail.status_code.return_value = 204
    mock_delete_mail = MagicMock(return_value=mock_mail)
    with patch("lementpro.services.users.Users.delete_mailbox", mock_delete_mail):
        response = Users().delete_mailbox(by_user=login)
        assert response.status_code() == 204


def test_put_notification_settings(login):
    mock_notify = MagicMock()
    mock_notify.status_code.return_value = 204
    mock_put_notify = MagicMock(return_value=mock_notify)
    with patch("lementpro.services.users.Users.put_notification_settings", mock_put_notify):
        response = Users().put_notification_settings(by_user=login, receiveNotificationByEmail=True)
        assert response.status_code() == 204


def test_get_notification_settings(login):
    mock_notify = MagicMock()
    mock_notify.json.return_value = {
        "receiveNotificationByEmail": True,
        "receiveNotificationOnNewObject": True,
        "receiveNotificationOnChangedObject": True,
        "receiveNotificationOnlyOnChangeInFavoriteObjects": True,
        "receiveNotificationOnMentioned": True,
        "receiveNotificationInVacation": True,
    }
    mock_notify.status_code.return_value = 200
    mock_get_notify = MagicMock(return_value=mock_notify)
    with patch("lementpro.services.users.Users.get_notification_settings", mock_get_notify):
        response = Users().get_notification_settings(by_user=login)
        assert response.status_code() == 200
        assert response.json()["receiveNotificationOnMentioned"] == True


def test_get_assistants(login):
    mock_assistants = MagicMock()
    mock_assistants.json.return_value = [
        {
            "id": 8,
            "assistantId": 3,
            "userName": "andranic",
            "email": "andranic@lement.pro",
            "displayName": "Андрей Шахраманьян",
            "avatarFileId": 35311,
            "isDisabled": False,
            "isDismissed": False,
        }
    ]
    mock_assistants.status_code.return_value = 200
    mock_get_assistants = MagicMock(return_value=mock_assistants)
    with patch("lementpro.services.users.Users.get_assistants", mock_get_assistants):
        response = Users().get_assistants(by_user=login)
        assert response.status_code() == 200
        assert response.json()[0]["userName"] == "andranic"
        assert response.json()[0]["displayName"] == "Андрей Шахраманьян"


def test_post_assistants(login):
    mock_assistants = MagicMock()
    mock_assistants.json.return_value = {"id": 10}
    mock_assistants.status_code.return_value = 200
    mock_post_assistants = MagicMock(return_value=mock_assistants)
    with patch("lementpro.services.users.Users.post_assistants", mock_post_assistants):
        response = Users().post_assistants(by_user=login, assistantId=10)
        assert response.status_code() == 200
        assert response.json()["id"] == 10


def test_userAssistantId(login):
    mock_assistants = MagicMock()
    mock_assistants.status_code.return_value = 204
    mock_delete_assistants = MagicMock(return_value=mock_assistants)
    with patch("lementpro.services.users.Users.userAssistantId", mock_delete_assistants):
        response = Users().userAssistantId(by_user=login, userAssistantId=10)
        assert response.status_code() == 204
