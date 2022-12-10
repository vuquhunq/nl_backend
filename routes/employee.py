

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from model.domain.items import OrganizationIDMOdel

route = APIRouter(tags=['Employee'], prefix='/employee')


@route.post('/get-employee')
async def get_items(orgs: OrganizationIDMOdel):
    return JSONResponse('Hello world', 200)