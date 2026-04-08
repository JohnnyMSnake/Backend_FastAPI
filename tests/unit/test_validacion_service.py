import pytest

from app.services.validacion_service import Validacion_Service


def test_validar_archivo_csv_devuelve_dataframe(csv_upload_file):
	service = Validacion_Service()
	dataframe = service.ValidarArchivo(csv_upload_file)

	assert len(dataframe) == 5
	assert {"fecha", "importe", "margen", "nombre_sucursal", "nombre_cliente", "nombre_vendedor", "nombre_linea", "kilogramos"}.issubset(dataframe.columns)

def test_validar_archivo_xlsx_devuelve_dataframe(xlsx_upload_file):
	service = Validacion_Service()
	dataframe = service.ValidarArchivo(xlsx_upload_file)

	assert len(dataframe) == 5
	assert {"fecha", "importe", "margen", "nombre_sucursal", "nombre_cliente", "nombre_vendedor", "nombre_linea", "kilogramos"}.issubset(dataframe.columns)

def test_validar_archivo_formato_no_soportado(unsupported_upload_file):
	service = Validacion_Service()

	with pytest.raises(ValueError, match="Formato no soportado"):
		service.ValidarArchivo(unsupported_upload_file)
