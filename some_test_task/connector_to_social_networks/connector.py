import requests

from .config import TOKEN_VK


class SocialNetworksConnector:
    def __init__(self, token: str):
        self._token = token
        self.proxies = {'http': '207.154.231.208:3128'}

    def get_profile(self, profile_id):
        pass

    def get_friends(self, profile_id):
        pass

    def get_wall(self, profile_id=None, domain=None):
        pass


class ConnectorToVK(SocialNetworksConnector):
    def __init__(self, token):
        SocialNetworksConnector.__init__(self, token=token)

        self._version = 5.103
        self._url = "https://api.vk.com/method/"
        self._method = {
            "users_get": "users.get",
            "friends_get": "friends.get",
            "wall_get": "wall.get",
        }

    def __new__(cls, token):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ConnectorToVK, cls).__new__(cls)
        return cls.instance

    def get_profile(self, profile_id):
        response = requests.get(self._url + self._method["users_get"],
                                params={
                                    "access_token": self._token,
                                    "v": self._version,
                                    "user_id": profile_id,
                                    "fields": 'photo_id,city'
                                },
                                proxies=self.proxies)
        data = response.json()
        return data

    def get_friends(self, profile_id):
        response = requests.get(self._url + self._method["friends_get"],
                                params={
                                    "access_token": self._token,
                                    "v": self._version,
                                    "user_id": profile_id,
                                    "count": 5,
                                    "fields": "nickname",
                                },
                                proxies=self.proxies)
        data = response.json()
        return data

    def get_wall(self, profile_id=None, domain=None):
        response = requests.get(self._url + self._method["wall_get"],
                                params={
                                    "access_token": self._token,
                                    "v": self._version,
                                    "domain": domain,
                                    "owner_id": profile_id,
                                    "count": 5,
                                },
                                proxies=self.proxies)
        data = response.json()
        return data
