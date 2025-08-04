import pytest
from requests import Response
from utils.api import vpns_bot_api

class TestRefInfo():

    @pytest.mark.order(11)
    def test_ref_info(self):
        print("Проверка реф кода")
        result_get: Response = vpns_bot_api.post_test_ref_info()
        assert result_get.status_code == 201