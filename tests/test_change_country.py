import pytest
from requests import Response
from utils.api import vpns_bot_api

class TestChangeConfigCountry():

    @pytest.mark.order(7)
    def test_change_country_is_200(self):
        print("Смена страны конфига")
        result_get: Response = vpns_bot_api.post_change_country()
        assert result_get.status_code == 201