# Maskify Backend

Maskify Backend is a FastAPI application designed to manage the backend functionality for an image inpainting widget. It enables users to upload images, draw masks, and export the resulting masked images. The application stores the original and mask images in MongoDB.

## Features

- Upload images via REST API.
- Automatically generate masks for uploaded images.
- Store image metadata (file paths) in MongoDB.
- Retrieve uploaded images and their masks using image IDs.
- Cross-Origin Resource Sharing (CORS) enabled for frontend integration.

---

## How to Run the Project Locally

Follow these steps to set up and run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/saurabh78crypto/maskify-backend.git
cd maskify-backend
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root of the project with the following content:
```python
MONGO_URL = "<your_mongodb_connection_string>"
```

### 5. Run the Server

Start the FastAPI server using Uvicorn:
```bash
uvicorn app.main:app --reload
```
The application will be available at `http://127.0.0.1:8000`.


## Libraries Used

- **FastAPI:** Web framework for building APIs.
- **Uvicorn:** ASGI server for running FastAPI.
- **Pydantic:** Data validation and settings management.
- **SQLAlchemy:** Database ORM.
- **Pillow:** For image processing.
- **Motor:** Async MongoDB driver for Python.
- **PyMongo:** MongoDB client.
- **Python-Multipart:** For handling file uploads.
- **Python-Dotenv:** Set the environment variables.