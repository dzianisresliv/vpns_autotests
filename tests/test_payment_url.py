import pytest
from requests import Response
from utils.api import vpns_bot_api

class TestPayment():

    @pytest.mark.order(8)
    def test_youkassa_is_201(self):
        print("Оплата через юкассу")
    result_get: Response = vpns_bot_api.youkassa_create_url()
    assert result_get.status_code == 201





