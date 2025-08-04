import pytest
from requests import Response
from utils.api import vpns_bot_api

class TestServerStatus():

    @pytest.mark.order(1)
    def test_status_is_200(self):
        print("Проверка доступности сервера")
        result_get: Response = vpns_bot_api.get_server_status()
        assert result_get.status_code == 200