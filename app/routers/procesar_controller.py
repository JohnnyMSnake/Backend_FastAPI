
from fastapi import APIRouter, HTTPException, UploadFile, File, Depends
from app.services.procesar_service import Procesar_Service
from app.dependencies import Procesar

router = APIRouter(prefix="/procesar", tags=["Procesar"])

@router.get("/")
def procesar_get():
    return "funciona el endpoint"

@router.post("/")
def procesar_post(file: UploadFile = File(...), Procesar_service: Procesar_Service = Depends(Procesar)):
    try:
        return Procesar_service.ProcesarArchivo(file)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))