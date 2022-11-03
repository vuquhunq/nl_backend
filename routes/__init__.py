from fastapi import APIRouter

from routes import auth, product

routes = APIRouter()

routes.include_router(auth.routes)
routes.include_router(product.routes)
