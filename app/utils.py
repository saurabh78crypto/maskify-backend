from PIL import Image as PILImage, ImageFilter
import os
from pathlib import Path
from fastapi import UploadFile
from app.database import db

UPLOAD_DIR = Path(__file__).parent / "uploads"

# Create upload directory if it doesn't exist
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

async def save_image_to_db(file: UploadFile):
    # Save the uploaded file to disk
    file_path = UPLOAD_DIR / file.filename
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Generate a mask (Example: Applying blur filter for demonstration)
    img = PILImage.open(file_path)
    mask_path = file_path.with_name(f"{file.filename.replace('.png', '')}_mask.png")
    
    # Apply some mask generation logic (blurred version in this case)
    mask = img.convert("LA").filter(ImageFilter.GaussianBlur(5))  # Simple grayscale + blur mask
    mask.save(mask_path)

    return str(file_path), str(mask_path)
