from app.services.procesar_service import Procesar_Service
from app.services.validacion_service import Validacion_Service


class DummyIaService:
	def generar_recomendacion(self, resultado):
		return "recomendacion"


def test_procesar_archivo_calcula_resumenes(csv_upload_file):
	service = Procesar_Service(Validacion_Service(), DummyIaService())
	resultado = service.ProcesarArchivo(csv_upload_file)

	assert resultado["importe_total"] == 10182.45
	assert resultado["ganancia_bruta"] == 866.66
	assert resultado["kilos_vendidos"] == 539.4
	assert resultado["importe_margen_cuatrimestre"] == [
		{"CUATRIMESTRE": 1, "IMPORTE_TOTAL": 10182.45, "MARGEN_TOTAL": 866.66}
	]
	assert resultado["margen_por_sucursal"] == [
		{"nombre_sucursal": "MAYOCAR", "MARGEN_TOTAL": 866.66}
	]
	assert resultado["importe_por_sucursal"] == [
		{"nombre_sucursal": "MAYOCAR", "IMPORTE_TOTAL": 10182.45}
	]
	assert resultado["top_clientes_margen"][0] == {
		"nombre_cliente": "SUPER MAYOREO DE CARNES DE PARRAL",
		"MARGEN_TOTAL": 630.0,
	}
	assert resultado["top_vendedores_margen"][0] == {
		"nombre_vendedor": "VENTAS IN HOUSE MAYOCAR",
		"MARGEN_TOTAL": 866.66,
	}
	assert resultado["margen_por_linea"][0] == {
		"nombre_linea": "ABARROTE",
		"MARGEN_TOTAL": 866.66,
	}


def test_procesar_archivo_elimina_duplicados(duplicated_csv_upload_file):
	service = Procesar_Service(Validacion_Service(), DummyIaService())
	resultado = service.ProcesarArchivo(duplicated_csv_upload_file)

	assert resultado["importe_total"] == 1502.82
	assert resultado["ganancia_bruta"] == 71.82
	assert resultado["kilos_vendidos"] == 86.4
