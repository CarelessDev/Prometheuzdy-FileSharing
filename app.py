from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path

from settings import *

app = FastAPI()

@app.post("/uploadfile/")
def upload_file(file: UploadFile = File(...)):
    try:
        file_path = Path(UPLOAD_DIR) / file.filename

        with file_path.open("wb") as buffer:
            buffer.write(file.file.read())
        
        return {"status": "ok"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/download/{filename}")
def download_file(filename: str):
    file_path = Path(UPLOAD_DIR) / filename
    print(file_path)
    if file_path.exists():
        return FileResponse(file_path, media_type="application/octet-stream", filename=filename)
    else:
        raise HTTPException(status_code=404, detail="File not found")
    
