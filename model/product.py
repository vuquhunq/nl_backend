from typing import Optional, TypeVar

from pydantic import BaseModel



class Product(BaseModel):
    id: str = None
    product_name: str
    

