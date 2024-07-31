import os
from typing import Union

from outline_vpn.outline_vpn import OutlineVPN
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from src.models.DynamicKey import DynamicKey
from src.models.OutlineKey import OutlineKey


class Outline:
    def __init__(self):
        self.api_url: str = os.getenv('API_URL')
        self.api_cert: str = os.getenv('API_CERT')
        self.client = OutlineVPN(self.api_url, self.api_cert)
        self.engine = create_engine(os.getenv('SERVER_DB'), echo=True)

    def get_dynamic_key(self, user_id: Union[str, int]) -> str:
        user_id = str(user_id)

        with Session(self.engine) as session:
            dynamic_key = (
                session.query(DynamicKey)
                .join(OutlineKey)
                .filter(OutlineKey.telegram_id == user_id)
                .first()
            )
            if dynamic_key:
                return dynamic_key.dynamic_outline_key

        raise ValueError(f'No dynamic key found for user {user_id}')

    def create_dynamic_key(self, user_id: Union[str, int]) -> str:
        user_id = str(user_id)
        key = self.client.create_key(name=f'key-{user_id}')
        with Session(self.engine) as session:
            outline_key = OutlineKey(
                telegram_id=user_id,
                name=key.name,
                password=key.password,
                port=key.port,
                method=key.method,
                access_url=key.access_url
            )
            dynamic_key = DynamicKey(
                outline_key=outline_key.id,
                dynamic_outline_key=self._generate_dynamic_key(user_id),
            )
            session.add_all([outline_key, dynamic_key])
            session.commit()

            return dynamic_key.dynamic_outline_key

    def _generate_dynamic_key(self, user_id: Union[str, int]) -> str:
        user_id = int(user_id)
        return f"{os.getenv('SERVER_HOST')}/conf/{os.getenv('OUTLINE_SALT')}?hex_id={hex(user_id)}"


if __name__ == '__main__':
    outline = Outline()
    print(outline.client.get_keys())
