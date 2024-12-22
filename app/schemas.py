from pydantic import BaseModel

class Image(BaseModel):
    original_image_path: str  
    mask_image_path: str      

    class Config:
        from_attributes = True
