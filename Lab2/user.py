import base_client
import requests


class user(base_client.BaseClient):
    vk_id = None
    username = None
    method = "users.get"

    def get_data(self):
        self.username = input()
        response = requests.get('https://api.vk.com/method/' + self.method + '?user_ids=' + self.username).json()
        self.vk_id = response["response"][0]["uid"]
