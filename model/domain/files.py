from pydantic import BaseModel, Field


class UrlImageModel(BaseModel):
    image_url: str = Field(
        default='/static/empty.jpg', alias='ImageURL')