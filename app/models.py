from pydantic import BaseModel
from typing import Optional

class Image(BaseModel):
    original_image_path: str
    mask_image_path: str

    class Config:
        # This tells Pydantic to handle MongoDB documents properly
        orm_mode = True

