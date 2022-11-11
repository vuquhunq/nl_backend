from typing import Optional, TypeVar

from pydantic import BaseModel

T = TypeVar('T')


class Response(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T] = None
