from fastapi import FastAPI

from study.rotas import router

app = FastAPI()

@app.get('/')
def get_root():
    return {'mensagem': 'api de papeis'}

app.include_router(router, prefix='')