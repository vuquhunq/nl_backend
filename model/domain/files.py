from pydantic import BaseModel, Field


class UrlImageModel(BaseModel):
    image_url: str = Field(
        default='https://picsum.photos/200', alias='ImageURL')
