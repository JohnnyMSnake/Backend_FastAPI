from pydantic import BaseModel


class data_importe_margen_cuatrimestre(BaseModel):
    CUATRIMESTRE: int
    IMPORTE_TOTAL: float
    MARGEN_TOTAL: float

class data_margen_por_sucursal(BaseModel):
    nombre_sucursal: str
    MARGEN_TOTAL: float

class data_importe_por_sucursal(BaseModel):
    nombre_sucursal: str
    IMPORTE_TOTAL: float

class data_top_clientes_margen(BaseModel):
    nombre_cliente: str
    MARGEN_TOTAL: float

class data_top_vendedores_margen(BaseModel):
    nombre_vendedor: str
    MARGEN_TOTAL: float

class data_margen_por_linea(BaseModel):
    nombre_linea: str
    MARGEN_TOTAL: float

class respuesta_total(BaseModel):
    importe_margen_cuatrimestre: list[data_importe_margen_cuatrimestre]
    margen_por_sucursal: list[data_margen_por_sucursal]
    importe_por_sucursal: list[data_importe_por_sucursal]
    top_clientes_margen: list[data_top_clientes_margen]
    top_vendedores_margen: list[data_top_vendedores_margen]
    margen_por_linea: list[data_margen_por_linea]
    importe_total: float
    ganancia_bruta: float
    kilos_vendidos: float
    recomendacion: str | None = None
    
