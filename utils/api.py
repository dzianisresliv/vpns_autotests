from utils.http_method import http_methods
import requests

base_url = "http://tg.karolom.com"  #Базовая URL

class vpns_bot_api():

    @staticmethod
    def create_new_trial():   #Метод создания нового конфига

        json_create_new_trial = {
            "tg_user_id": 693130475,
            "tg_user_name": "dzianis7",
            "tg_full_name": "Dzianis",
            "invite_code": "assda"
        }

        post_resource = "/v2/bot/subscriptions/trial"  #ресурс метода POST
        post_url = (base_url + post_resource)
        print(post_url)
        result_post = http_methods.post(post_url, json_create_new_trial)
        print(result_post.text)
        return result_post

    @staticmethod
    def get_server_status():
        base_url = "http://tg.karolom.com"
        get_resource = "/v2/bot/test"
        get_url = (base_url + get_resource)
        print(get_url)
        result_get = http_methods.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def test_subscriptios_clear():
        base_url = "http://tg.karolom.com"
        bearer_token = "89dff937ad145a3893cf3a3af9276879"
        headers = {
            "Authorization": f"Bearer {bearer_token}",
            "Content-Type": "application/json"
        }
        post_resource = "/v2/bot/subscriptions/clear"
        post_url = (base_url + post_resource)
        print(post_url)

        json_create_new_trial = {
            "tg_user_id": 693130475
        }

        result_post = requests.post(post_url, headers=headers, json=json_create_new_trial)
        print("Ответ сервера: ", result_post.text)
        print("Статус код: ", result_post.status_code)
        return result_post

    @staticmethod
    def get_subscription_status():
        base_url = "http://tg.karolom.com"
        bearer_token = "89dff937ad145a3893cf3a3af9276879"
        headers = {
            "Authorization": f"Bearer {bearer_token}",
            "Content-Type": "application/json"
        }
        post_resource = "/v2/bot/subscriptions/status"
        post_url = (base_url + post_resource)
        print(post_url)

        json_create_new_trial = {
            "tg_user_id": 693130475
        }

        result_post = requests.post(post_url, headers=headers, json=json_create_new_trial)
        print("Ответ сервера:", result_post.text)
        print("Статус код:", result_post.status_code)

        check_post = result_post.json()
        check_info_post = check_post.get("success")
        print("Ответ сервера (success):", check_info_post)
        if check_info_post is True:
            print("пользователь имеет активную подписку")
        else:
            print("подписка отсутствует")
        return result_post
