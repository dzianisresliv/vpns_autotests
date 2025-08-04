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

    @staticmethod
    def post_generate_adv():
            base_url = "http://tg.karolom.com"
            bearer_token = "89dff937ad145a3893cf3a3af9276879"
            headers = {
                "Authorization": f"Bearer {bearer_token}",
                "Content-Type": "application/json"
            }
            post_resource = "/v2/bot/config/generate"
            post_url = (base_url + post_resource)
            print(post_url)

            json_create_new_trial = {
                "tg_user_id": 693130475,
                "adv": "true",
                "invite_code": "assda"
            }

            result_post = requests.post(post_url, headers=headers, json=json_create_new_trial)
            print("Ответ сервера:", result_post.text)
            print("Статус код:", result_post.status_code)
            if result_post.status_code == 201:
                print("Скачайте новый конфиг")
            else:
                print("Вы уже получили конфигурацию")
            return result_post


    @staticmethod
    def post_config_list():
            base_url = "http://tg.karolom.com"
            bearer_token = "89dff937ad145a3893cf3a3af9276879"
            headers = {
                "Authorization": f"Bearer {bearer_token}",
                "Content-Type": "application/json"
            }
            post_resource = "/v2/bot/config/list"
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
            if check_info_post is True:
                subscriptions = check_post.get("data", [])
                active_sub_count = len(subscriptions)
                print("Число ваших действующих подписок (number):", active_sub_count)

                if active_sub_count > 0:
                    print("Пользователь активную(ые) подписку(и)")
                else:
                    print("Подписка отсутствует")
            else:
                print(" Ошибка выполнения запроса, сервер не отвечает")

            return result_post

    @staticmethod
    def post_change_country():
        base_url = "http://tg.karolom.com"
        bearer_token = "89dff937ad145a3893cf3a3af9276879"
        headers = {
            "Authorization": f"Bearer {bearer_token}",
            "Content-Type": "application/json"
        }
        post_resource = "/v2/bot/config/change_country"
        post_url = (base_url + post_resource)
        print(post_url)

        json_create_change_country = {
            "tg_user_id": 693130475,
            "country_сode": "DE"
        }

        result_post = requests.post(post_url, headers=headers, json=json_create_change_country)
        print("Ответ сервера:", result_post.text)
        print("Статус код:", result_post.status_code)

        if result_post.status_code == 201:
            print("Cтрана конфигурации изменена")
        else:
            print("Ошибка, повторите попытку")

        return result_post