import requests


class APIService:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=headers)
        return response

    def post(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=data, headers=headers)
        return response

    def put(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, json=data, headers=headers)
        return response

    def delete(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url, headers=headers)
        return response
