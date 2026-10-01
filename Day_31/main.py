import os
import uuid
import magic
from pathlib import Path
from fastapi import FastAPI, File, UploadFile, HTTPException, status
from werkzeug.utils import secure_filename

app = FastAPI(title="Secure File Upload API")

# Configuration
UPLOAD_DIR = Path("safe_storage")
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB limit
ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".pdf"}
ALLOWED_MIME_TYPES = {
    "image/png",
    "image/jpeg",
    "application/pdf",
}

# Ensure storage directory exists
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@app.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload_file(file: UploadFile = File(...)):
    # 1. Check for filename presence
    if not file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No filename provided."
        )

    # 2. Sanitize original filename and validate extension
    clean_name = secure_filename(file.filename)
    extension = Path(clean_name).suffix.lower()
    
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Extension '{extension}' is not allowed."
        )

    # 3. Read first chunk for Magic Byte (MIME) validation
    header_chunk = await file.read(2048)
    detected_mime = magic.from_buffer(header_chunk, mime=True)

    if detected_mime not in ALLOWED_MIME_TYPES:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=f"Invalid file content type: {detected_mime}."
        )

    # 4. Stream and enforce size limit without loading whole file into RAM
    unique_filename = f"{uuid.uuid4().hex}{extension}"
    target_path = UPLOAD_DIR.resolve() / unique_filename

    # Ensure path stays inside upload directory (path traversal check)
    if not str(target_path).startswith(str(UPLOAD_DIR.resolve())):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid destination path."
        )

    bytes_written = len(header_chunk)
    
    try:
        with open(target_path, "wb") as out_file:
            out_file.write(header_chunk)
            
            while chunk := await file.read(1024 * 1024):  # 1 MB chunks
                bytes_written += len(chunk)
                if bytes_written > MAX_FILE_SIZE:
                    # Clean up partial file before raising error
                    out_file.close()
                    if target_path.exists():
                        target_path.unlink()
                    raise HTTPException(
                        status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                        detail=f"File exceeds maximum allowed size of {MAX_FILE_SIZE // (1024 * 1024)} MB."
                    )
                out_file.write(chunk)
    except HTTPException:
        raise
    except Exception as exc:
        if target_path.exists():
            target_path.unlink()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred while saving the file."
        )

    return {
        "message": "File uploaded successfully",
        "stored_filename": unique_filename,
        "original_filename": clean_name,
        "size_bytes": bytes_written,
        "mime_type": detected_mime,
    }
