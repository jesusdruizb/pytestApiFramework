import requests


class RestRequests:

    def __int__(self):
        pass

    def get_request(self,url, params = ''):
        return requests.get(url, params=params)

