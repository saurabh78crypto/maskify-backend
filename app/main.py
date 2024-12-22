from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.responses import JSONResponse
from app.utils import save_image_to_db
from app.schemas import Image
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from app.database import db 

app = FastAPI()

# Add CORSMiddleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict it to certain domains if needed
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    try:
        # Save the uploaded file and generate a mask image
        file_path, mask_path = await save_image_to_db(file)

        # Save image details in MongoDB
        image_details = {
            "original_image_path": file_path,
            "mask_image_path": mask_path
        }

         # Insert into MongoDB
        result = await db.images.insert_one(image_details)

        return {"message": "Image uploaded successfully", "image_id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to upload image or save to database: {str(e)}")

@app.get("/images/{image_id}")
async def get_image(image_id: str):
    try:
        image = await db.images.find_one({"_id": image_id})
        if not image:
            raise HTTPException(status_code=404, detail="Image not found")
        
        image_data = jsonable_encoder(image)
        return image_data
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to retrieve image from database")
