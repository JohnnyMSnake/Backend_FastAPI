from fastapi import UploadFile, HTTPException

#Service encargado de validar el arhivo
class Validacion_Service():
    def ValidarArchivo(self, file: UploadFile) -> str:
        if not file or not file.filename:
            raise HTTPException(status_code=400, detail="Archivo invalido")
    
        extension = file.filename.lower().split(".")[-1]

        if extension not in ["csv", "xlsx"]:
            raise HTTPException(status_code=400, detail="Solo se permite extensiones .csv o .xlsx")
        
        return "Archivo aceptado"