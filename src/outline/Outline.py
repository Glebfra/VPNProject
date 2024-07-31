import os

from outline_vpn.outline_vpn import OutlineVPN
from sqlalchemy import create_engine


class Outline:
    api_url: str = os.getenv('API_URL')
    api_cert: str = os.getenv('API_CERT')

    def __init__(self):
        self.client = OutlineVPN(self.api_url, self.api_cert)
        self.engine = create_engine(os.getenv('SERVER_DB'), echo=True)

    def bytes_to_gbytes(self, bytes):
        return bytes / (1024 ** 3)

    def gbytes_to_bytes(self, gbytes):
        return gbytes * (1024 ** 3)


if __name__ == '__main__':
    outline = Outline()
    print(outline.client.get_keys())
