import pytest
from requests import Response
from utils.api import vpns_bot_api

class TestSubscriptionsStatus():

    @pytest.mark.order(4)
    def test_subscriptios_status_is_True(self):
        print("Проверка статуса подписки")
        result_post: Response = vpns_bot_api.get_subscription_status()
        assert result_post.json().get("success") is True