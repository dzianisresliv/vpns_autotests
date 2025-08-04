import pytest
from requests import Response
from utils.api import vpns_bot_api

class TestConfigList():

    @pytest.mark.order(7)
    def test_config_list_existed(self):
        print("Список доступных конфигов пользователя")
        result_get: Response = vpns_bot_api.post_config_list()
        assert result_get.status_code == 201