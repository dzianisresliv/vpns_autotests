import pytest
from requests import Response
from utils.api import vpns_bot_api

class TestNewSupportTicket():

    @pytest.mark.order(10)
    def test_new_support_ticket(self):
        print("Проверка доступности сервера")
        result_get: Response = vpns_bot_api.post_create_support_ticket()
        assert result_get.status_code == 201