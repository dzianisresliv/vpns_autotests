import pytest
from requests import Response
from utils.api import vpns_bot_api

class TestSubscriptiosClear():

    @pytest.mark.order(3)
    def test_subs_cleared(self):
        print("Удаление подписки")
        result_post: Response = vpns_bot_api.test_subscriptios_clear()
        assert result_post.status_code == 201


