from fastapi import APIRouter

routes = APIRouter(tags=['Products'], prefix='/products')


@routes.get('/')
async def root():
    return 'Hello wrodl'
