import pytest
from requests import Response
from utils.api import vpns_bot_api

class Test_create_new_config:  #cоздание триального конфига

    @pytest.mark.order(2)
    def test_create_new_config(self):
        print("Метод POST new")
        result_post: Response = vpns_bot_api.create_new_trial()
        assert result_post.status_code == 201

