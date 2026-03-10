from fastapi import UploadFile, HTTPException
import pandas as pd
#Service encargado de validar el arhivo
class Validacion_Service():
    def ValidarArchivo(self, file: UploadFile) -> pd.DataFrame:
        try:
            # Leer según la extensión
            extension = file.filename.lower().split(".")[-1]
            
            if extension == "xlsx":
                df = pd.read_excel(file.file, engine='openpyxl')
            elif extension == "csv":
                df = pd.read_csv(file.file)
            else:
                raise HTTPException(status_code=400, detail="Formato no soportado")
                
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error al leer archivo: {str(e)}")
        
        return df