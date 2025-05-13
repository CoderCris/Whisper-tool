from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from services.file_service import process_whisper_file, WhisperProcessingError
from pathlib import Path
import shutil

app = FastAPI()

# Habilitar CORS para desarrollo local con React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = Path("uploads")
OUTPUT_DIR = Path("output")
UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

@app.post("/process")
def process_file(file: UploadFile = File(...)):
    try:
        input_path = UPLOAD_DIR / file.filename
        output_path = OUTPUT_DIR / f"cleaned_{file.filename}"

        with input_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        result_path = process_whisper_file(str(input_path), str(output_path))

        return {"message": "Archivo procesado exitosamente.", "output_path": result_path}
    except WhisperProcessingError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inesperado: {e}")
