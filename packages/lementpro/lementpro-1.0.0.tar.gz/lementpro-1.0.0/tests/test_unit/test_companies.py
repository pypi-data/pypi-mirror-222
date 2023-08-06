from unittest.mock import patch, MagicMock
from lementpro.services.companies import Companies


def test_get_companies_info(login):
    mock_companies = MagicMock()
    mock_companies.json.return_value = {
        "companyId": 1,
        "name": "lementtest",
        "isReadOnly": False,
        "isDisabled": False,
        "isSchemaReadonly": False,
        "timeZone": "Europe/Moscow",
        "siteIconFile": 254,
        "siteLogoFile": 3525,
        "siteName": "SODIS LAB",
    }
    mock_companies.status_code.return_value = 200
    mock_info = MagicMock(return_value=mock_companies)
    with patch("lementpro.services.companies.Companies.info", mock_info):
        response = Companies().info(by_user=login)
        assert response.json()["name"] == "lementtest"
        assert response.status_code() == 200
