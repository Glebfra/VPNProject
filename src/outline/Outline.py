import os

from dotenv import load_dotenv
from outline_vpn.outline_vpn import OutlineVPN
from sqlalchemy import create_engine, select, delete
from sqlalchemy.orm import Session

from src.models.OutlineKey import OutlineKey

load_dotenv('../../.env')


class Outline:
    api_url: str = os.getenv('API_URL')
    api_cert: str = os.getenv('API_CERT')

    def __init__(self):
        self.client = OutlineVPN(self.api_url, self.api_cert)
        self.engine = create_engine(os.getenv('SERVER_DB'), echo=True)

    def add_key(self, name: str):
        key = self.client.create_key(name=name)
        model_key = OutlineKey(
            id=key.key_id,
            name=key.name,
            password=key.password,
            port=key.port,
            method=key.method,
            access_url=key.access_url
        )

        with Session(self.engine) as session:
            session.add(model_key)
            session.commit()

    def bytes_to_gbytes(self, bytes):
        return bytes / (1024 ** 3)

    def gbytes_to_bytes(self, gbytes):
        return gbytes * (1024 ** 3)


if __name__ == '__main__':
    outline = Outline()
    print(outline.client.get_keys())
