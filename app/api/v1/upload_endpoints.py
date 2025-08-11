import os
from uuid import uuid4
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse

UPLOAD_DIR = "static"
os.makedirs(UPLOAD_DIR, exist_ok=True)

upload_router = APIRouter(prefix="/upload", tags=["Upload"])


@upload_router.post("/logo")
async def upload_logo(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Файл має бути зображенням")

    file_ext = file.filename.split('.')[-1]
    filename = f"{uuid4().hex}.{file_ext}"
    filepath = os.path.join(UPLOAD_DIR, filename)

    # Збереження файлу
    with open(filepath, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    url = f"/static/{filename}"
    return JSONResponse(content={"url": url})
