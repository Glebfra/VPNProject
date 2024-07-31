import os
from typing import Union

from outline_vpn.outline_vpn import OutlineVPN
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from src.models.DynamicKey import DynamicKey
from src.models.OutlineKey import OutlineKey


class Outline:
    api_url: str = os.getenv('API_URL')
    api_cert: str = os.getenv('API_CERT')

    def __init__(self):
        self.client = OutlineVPN(self.api_url, self.api_cert)
        self.engine = create_engine(os.getenv('SERVER_DB'), echo=True)

    def get_dynamic_key(self, user_id: Union[str, int]) -> str:
        user_id = str(user_id)

        with Session(self.engine) as session:
            statement = (
                select(DynamicKey)
                .join(DynamicKey.outline_key)
                .where(OutlineKey.telegram_id == user_id)
            )
            dynamic_key = session.scalar(statement)
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
                outline_key=outline_key,
                dynamic_outline_key=self.get_dynamic_key(user_id),
            )
            session.add_all([outline_key, dynamic_key])
            session.commit()

            return dynamic_key.dynamic_outline_key

    def generate_dynamic_key(self, user_id: Union[str, int]) -> str:
        user_id = int(user_id)
        return f"{os.getenv('SERVER_HOST')}/conf/{os.getenv('OUTLINE_SALT')}?hex_id={hex(user_id)}"


if __name__ == '__main__':
    outline = Outline()
    print(outline.client.get_keys())
