from fastapi import UploadFile, HTTPException
import pandas as pd
#Service encargado de validar el arhivo
class Validacion_Service():
    def ValidarArchivo(self, file: UploadFile) -> pd.DataFrame:
        # Leer según la extensión
        extension = file.filename.lower().split(".")[-1]
            
        if extension == "xlsx":
            df = pd.read_excel(file.file, engine='openpyxl')
            
            #Aqui esta bizarro, lo hizo copilot, 
            #al parecer lo que hace es probar todas las decodificaciones posibles
            #y calarlo con eso, en caso de que falle, volver a lo que era antes
        elif extension == "csv":
            df = None
            csv_encodings = ["utf-8-sig", "utf-8", "latin1", "cp1252"]
            last_decode_error = None

            for encoding in csv_encodings:
                try:
                    file.file.seek(0)
                    df = pd.read_csv(file.file, encoding=encoding)
                    break
                except UnicodeDecodeError as e:
                    last_decode_error = e

            if df is None:
                raise ValueError(f"No se pudo decodificar el CSV con codificaciones conocidas: {last_decode_error}")
        else:
            raise ValueError("Formato no soportado")
        
        return df