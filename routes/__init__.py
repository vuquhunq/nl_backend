from fastapi import APIRouter

from routes import auth, items, organization

routes = APIRouter()

routes.include_router(auth.route)
routes.include_router(organization.route)
routes.include_router(items.route)
