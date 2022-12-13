from fastapi import APIRouter

from routes import (auth, brand, customer, employee, file, items, order,
                    organization, unit)

routes = APIRouter()

routes.include_router(auth.route)
routes.include_router(organization.route)
routes.include_router(items.route)
routes.include_router(employee.route)
routes.include_router(file.routes) 
routes.include_router(customer.routes) 
routes.include_router(order.routes) 
routes.include_router(unit.routes)
routes.include_router(brand.routes)