from fastapi import APIRouter

from routes import product, user

routes = APIRouter()

routes.include_router(user.routes)
routes.include_router(product.routes)
