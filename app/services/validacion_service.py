from fastapi import UploadFile, HTTPException
import pandas as pd
#Service encargado de validar el arhivo
class Validacion_Service():
    def ValidarArchivo(self, file: UploadFile) -> pd.DataFrame:
        # Leer según la extensión
        extension = file.filename.lower().split(".")[-1]
            
        if extension == "xlsx":
            df = pd.read_excel(file.file, engine='openpyxl')
        elif extension == "csv":
            df = pd.read_csv(file.file)
        else:
            raise ValueError("Formato no soportado")
        
        return df