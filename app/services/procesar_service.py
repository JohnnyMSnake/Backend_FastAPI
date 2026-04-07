import os
import pandas as pd
from fastapi import UploadFile

from app.services.validacion_service import Validacion_Service
from app.services.ia_service import Ia_Service

class Procesar_Service():

    def __init__(self, Validar_Service: Validacion_Service, Ia_Service: Ia_Service):
        self.Validar_Service = Validar_Service
        self.Ia_Service = Ia_Service


    def ProcesarArchivo(self, file: UploadFile):
        
        df = self.Validar_Service.ValidarArchivo(file)
        
        try:
            # eliminar duplicados
            df = df.drop_duplicates()

            # los strings vacios se rellenan a sin dato y los numericos a 0
            for col in df.select_dtypes(include=["object", "string"]).columns:
                df[col] = df[col].fillna("SIN DATO")

            for col in df.select_dtypes(include=["number"]).columns:
                df[col] = df[col].fillna(0)

            # hacer que fecha sea datetime
            if "fecha" in df.columns:
                #df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
                #NOTA: el formato original del excel esta volteado el mes y el dia
                # por lo que el perro siempre detectaba todo en Enero 
                 
                df["fecha"] = pd.to_datetime(df["fecha"], dayfirst=True, errors="coerce")

            # poner todo en mayusculas
            for col in df.select_dtypes(include=["object", "string"]).columns:
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
                    .round(2)
                    .sort_values("CUATRIMESTRE")
            )

            # margen por sucursal
            margen_por_sucursal = (
                df.groupby("nombre_sucursal", as_index=False)
                    .agg(MARGEN_TOTAL=("margen", "sum"))
                    .round(2)
                    .sort_values("MARGEN_TOTAL", ascending=False)
            )

            # importe por sucursal
            importe_por_sucursal = (
                df.groupby("nombre_sucursal", as_index=False)
                    .agg(IMPORTE_TOTAL=("importe", "sum"))
                    .round(2)
                    .sort_values("IMPORTE_TOTAL", ascending=False)
            )

            # clientes con mas margen
            top_clientes_margen = (
                df.groupby("nombre_cliente", as_index=False)
                    .agg(MARGEN_TOTAL=("margen", "sum"))
                    .round(2)
                    .sort_values("MARGEN_TOTAL", ascending=False)
                    .head(10)
            )

            # vendedores con mas margen
            top_vendedores_margen = (
                df.groupby("nombre_vendedor", as_index=False)
                    .agg(MARGEN_TOTAL=("margen", "sum"))
                    .round(2)
                    .sort_values("MARGEN_TOTAL", ascending=False)
                    .head(10)
            )

            # margen por linea
            margen_por_linea = (
                df.groupby("nombre_linea", as_index=False)
                    .agg(MARGEN_TOTAL=("margen", "sum"))
                    .round(2)
                    .sort_values("MARGEN_TOTAL", ascending=False)
            )

            # sacar totales
            ganancia_bruta = round(df["margen"].sum(), 2)
            kilos_vendidos = round(df["kilogramos"].sum(), 2)
            importe_total = round(df["importe"].sum(), 2)

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

            #NOTA: Siempre que se quiera depurar la info de los datos, 
            #comentar estas 2 lineas para evitar gastar tokes
            
            #recomendacion = self.Ia_Service.generar_recomendacion(resultado)
            #resultado["recomendacion"] = recomendacion

            return resultado
            
        except Exception as e:
            raise RuntimeError(f"Error al procesar datos: {str(e)}")