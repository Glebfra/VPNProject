import os
from typing import Union

from outline_vpn.outline_vpn import OutlineKey, OutlineVPN
from sqlalchemy import create_engine


class Outline:
    api_url: str = os.getenv('API_URL')
    api_cert: str = os.getenv('API_CERT')

    def __init__(self):
        self.client = OutlineVPN(self.api_url, self.api_cert)
        self.engine = create_engine(os.getenv('SERVER_DB'), echo=True)

    def generate_dynamic_key(self, user_id: Union[str, int]) -> str:
        user_id = int(user_id)
        return f"{os.getenv('SERVER_HOST')}/conf/{os.getenv('OUTLINE_SALT')}?hex_id={hex(user_id)}"

    def create_new_key(self, name) -> OutlineKey:
        return self.client.create_key(name=name)


if __name__ == '__main__':
    outline = Outline()
    print(outline.client.get_keys())
