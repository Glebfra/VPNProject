import os

from outline_api import Manager, get_active_keys, get_key_numbers
from dotenv import load_dotenv


class Outline:
    api_url: str = os.getenv('API_URL')
    api_cert: str = os.getenv('API_CERT')

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Outline, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.manager = Manager(self.api_url, self.api_cert)


if __name__ == '__main__':
    outline = Outline()
