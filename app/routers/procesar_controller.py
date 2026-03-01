from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter(prefix="/procesar", tags=["Procesar"])

@router.get("/")
def procesar_get():
    return "funciona el endpoint"

@router.post("/")
def procesar_post(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="Archivo invalido")
    
    extension = file.filename.lower().split(".")[-1]

    if extension not in ["csv", "xlsx"]:
        raise HTTPException(status_code=400, detail="Solo se permite extensiones .csv o .xlsx")
    
    return "Archivo aceptado"
