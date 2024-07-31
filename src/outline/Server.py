import os

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def index():
    return {'message': 'Hello World!', 'salt': os.getenv('OUTLINE_SALT')}


@app.get('/conf/%s{hex_id}' % os.getenv('OUTLINE_SALT'))
async def handle_connection(hex_id: str):
    return {'id': hex_id}
