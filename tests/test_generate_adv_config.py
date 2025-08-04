import pytest
from requests import Response
from utils.api import vpns_bot_api

class TestGenerateAdvConfig():

    @pytest.mark.order(5)
    def test_generate_adv_config_is_200(self):
        print("Создание конфига с рекламой")
        result_get: Response = vpns_bot_api.post_generate_adv()
        assert result_get.status_code == 201