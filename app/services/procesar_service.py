import os
import pandas as pd
from fastapi import HTTPException

class Procesar_service():
    def ProcesarArchivo(self, file):
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

        try:
            # eliminar duplicados
            df = df.drop_duplicates()

            # los strings vacios se rellenan a sin dato y los numericos a 0
            for col in df.select_dtypes(include="object").columns:
                df[col] = df[col].fillna("SIN DATO")

            for col in df.select_dtypes(include=["number"]).columns:
                df[col] = df[col].fillna(0)

            # hacer que fecha sea datetime
            if "fecha" in df.columns:
                df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")

            # poner todo en mayusculas
            for col in df.select_dtypes(include="object").columns:
                # evita que NaN se convierta en 'NAN' 
                df[col] = df[col].astype(str).str.strip().str.upper()

            # margen por cuatrimestre
            # los cuatrimestres se dividen como: 1 = enero-abril, 2 = mayo-agosto, 3 = septiembre-diciembre
            df["MES"] = df["fecha"].dt.month
            df["CUATRIMESTRE"] = ((df["MES"] - 1) // 4) + 1

            importe_margen_cuatrimestre = (
                df.groupby("CUATRIMESTRE", as_index=False)
                    .agg(IMPORTE_TOTAL=("importe", "sum"),
                        MARGEN_TOTAL=("margen", "sum"))
                    .sort_values("CUATRIMESTRE")
            )

            # margen por sucursal
            margen_por_sucursal = (
                df.groupby("nombre_sucursal", as_index=False)
                    .agg(MARGEN_TOTAL=("margen", "sum"))
                    .sort_values("MARGEN_TOTAL", ascending=False)
            )

            # importe por sucursal
            importe_por_sucursal = (
                df.groupby("nombre_sucursal", as_index=False)
                    .agg(IMPORTE_TOTAL=("importe", "sum"))
                    .sort_values("IMPORTE_TOTAL", ascending=False)
            )

            # clientes con mas margen
            top_clientes_margen = (
                df.groupby("nombre_cliente", as_index=False)
                    .agg(MARGEN_TOTAL=("margen", "sum"))
                    .sort_values("MARGEN_TOTAL", ascending=False)
                    .head(10)
            )

            # vendedores con mas margen
            top_vendedores_margen = (
                df.groupby("nombre_vendedor", as_index=False)
                    .agg(MARGEN_TOTAL=("margen", "sum"))
                    .sort_values("MARGEN_TOTAL", ascending=False)
                    .head(10)
            )

            # margen por linea
            margen_por_linea = (
                df.groupby("nombre_linea", as_index=False)
                    .agg(MARGEN_TOTAL=("margen", "sum"))
                    .sort_values("MARGEN_TOTAL", ascending=False)
            )

            # sacar totales
            ganancia_bruta = df["margen"].sum()
            kilos_vendidos = df["kilogramos"].sum()
            importe_total = df["importe"].sum()

            # convertir a diccionario para enviar al frontend
            resultado = {
                "importe_margen_cuatrimestre": importe_margen_cuatrimestre.to_dict(orient="records"),
                "margen_por_sucursal": margen_por_sucursal.to_dict(orient="records"),
                "importe_por_sucursal": importe_por_sucursal.to_dict(orient="records"),
                "top_clientes_margen": top_clientes_margen.to_dict(orient="records"),
                "top_vendedores_margen": top_vendedores_margen.to_dict(orient="records"),
                "margen_por_linea": margen_por_linea.to_dict(orient="records"),
                "importe_total": importe_total,
                "ganancia_bruta": ganancia_bruta,
                "kilos_vendidos": kilos_vendidos
            }

            return resultado
            
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error al procesar datos: {str(e)}")