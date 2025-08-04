import pytest
from requests import Response
from utils.api import vpns_bot_api

class TestUseDiscount():

    @pytest.mark.order(9)
    def test_youkassa_is_201(self):
        print("Использовать скидку для покупки конфига")

    result_get: Response = vpns_bot_api.new_discount_subs()
    assert result_get.status_code == 201