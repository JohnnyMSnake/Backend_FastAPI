from random import random

from fastapi import APIRouter, UploadFile, File, Depends
from app.services.procesar_service import Procesar_Service
from app.services.validacion_service import Validacion_Service
from app.dependencies import Procesar, Validacion

router = APIRouter(prefix="/procesar", tags=["Procesar"])

@router.get("/")
def procesar_get():
    return "funciona el endpoint"

@router.post("/")
def procesar_post(file: UploadFile = File(...), Validar_Service: Validacion_Service = Depends(Validacion), Procesar_service: Procesar_Service = Depends(Procesar)):
    Validar_Service.ValidarArchivo(file)
    
    # resetear el puntero (no entendi pq se mueve al validar xd)
    file.file.seek(0)
    
    return Procesar_service.ProcesarArchivo(file)