import base_client
import user
import requests
import datetime
import matplotlib


class friend_list(base_client.BaseClient):
    response = None
    today = datetime.datetime.today()
    stats = []

    def get_resp(self, id):
        self.response = requests.get(
            'https://api.vk.com/method/friends.get?user_id=' + str(id) + '&fields=bdate&v=5.62').json()
        return 0

    def get_headers(self):

        for i in self.response["response"]['items']:
            if ('bdate' not in i):
                continue
            if (len(i['bdate']) > 5):
                d = datetime.datetime.strptime(i['bdate'], "%d.%m.%Y")
                y = int((str((self.today - d) / 365)[0:2]))
                self.stats.append(y)
