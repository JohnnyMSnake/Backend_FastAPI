from fastapi import APIRouter, UploadFile, File, Depends
from app.services.validacion_service import Validacion_Service
from app.dependencies import Validacion

router = APIRouter(prefix="/procesar", tags=["Procesar"])

@router.get("/")
def procesar_get():
    return "funciona el endpoint"

@router.post("/")
def procesar_post(file: UploadFile = File(...), Validar_Service: Validacion_Service = Depends(Validacion)):
    return Validar_Service.ValidarArchivo(file)
