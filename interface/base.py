import requests
from conf.default import DefaultConfig


class BaseRequest:
    session = requests.Session()



    def __init__(self, base_url=DefaultConfig.base_url):
        self.base_url = base_url

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


    @staticmethod
    def get_full_url(base, number):
        return f"{base}{number}"

    @staticmethod
    def check_count(data):
        return data.json().get("count")

    @staticmethod
    def get_result(data):
        return data.json().get("result")

    def get_first_result(self, data):
        return self.get(data)[0]

    def get_last_result(self, data):
        return self.get(data)[-1]

    def get(self, url, *args, **kwargs):
        url = self.base_url + url
        return self.session.get(url=url, *args, **kwargs)

    def delete(self, url, *args, **kwargs):
        url = self.base_url + url
        return self.session.delete(url, *args, **kwargs)

    def post(self, url, *args, **kwargs):
        url = self.base_url + url
        return self.session.post(url=url, *args, **kwargs)
    
    def put(self, url, *args, **kwargs):
        url = self.base_url + url
        return self.session.put(url, *args, **kwargs)

