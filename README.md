**Proyecto**

- **Nombre:** Backend_FastAPI — API para procesar archivos de ventas y calcular métricas.

**Resumen**

- **Descripción:** Servicio FastAPI que recibe un archivo (CSV/XLSX), valida y normaliza los datos, calcula resúmenes (importe, margen, kilos) por cuatrimestre, sucursal, línea, top clientes/vendedores, y devuelve un objeto JSON con las métricas. Opcionalmente genera recomendaciones usando un servicio externo de IA.

**Estructura del repositorio**

- **`app/`**: Código de la aplicación.

  - [app/main.py](app/main.py): Punto de entrada y registro de routers.
  - [app/routers/procesar_controller.py](app/routers/procesar_controller.py): Endpoint `/procesar` (GET, POST).
  - [app/services/validacion_service.py](app/services/validacion_service.py): Lectura y validación de archivos (CSV/XLSX).
  - [app/services/procesar_service.py](app/services/procesar_service.py): Lógica de procesamiento y generación de resúmenes.
  - [app/services/ia_service.py](app/services/ia_service.py): Cliente opcional para generar recomendaciones (usa `GROQ_API_KEY`).
  - [app/schemas/response_schema.py](app/schemas/response_schema.py): Schemas Pydantic de la respuesta.
  - [app/core/config.py](app/core/config.py): Configuración (CORS, variables de entorno).
  - [app/core/cors.py](app/core/cors.py): Middleware CORS.
  - [app/dependencies.py](app/dependencies.py): Fábrica de dependencias (inyección manual).
- **`tests/`**: Tests unitarios y fixtures (usar `pytest`).

**Requisitos**

- **Python:** 3.10+ (recomendado).
- **Dependencias:** instalar con `pip install -r requirements.txt`.

**Instalación rápida**

- Crear y activar entorno virtual:

```
python -m venv venv
venv\Scripts\Activate.ps1   # Windows PowerShell
```

- Instalar dependencias:

```
pip install -r requirements.txt
```

**Ejecución**

- Levantar la API en modo desarrollo:

```
uvicorn app.main:app --reload
```

- Documentación interactiva (Swagger): http://127.0.0.1:8000/docs

**Endpoints principales**

- **GET** `/procesar/` — Salud básico. (Ver [app/routers/procesar_controller.py](app/routers/procesar_controller.py))
- **POST** `/procesar/` — Subir archivo (`multipart/form-data`, campo `file`). Responde con el schema `respuesta_total` definido en [app/schemas/response_schema.py](app/schemas/response_schema.py).

Formato esperado: CSV o XLSX. Si el formato no es soportado, se devuelve error 400.

**Descripción de servicios clave**

- **`Validacion_Service`** ([app/services/validacion_service.py](app/services/validacion_service.py)): Lee el archivo según extensión (`.xlsx` con `openpyxl`, `.csv` probando varias codificaciones) y devuelve un `pandas.DataFrame`.
- **`Procesar_Service`** ([app/services/procesar_service.py](app/services/procesar_service.py)): Normaliza datos (rellena NaN, mayúsculas, parsea fecha con `dayfirst=True`), elimina duplicados y calcula:
  - `importe_margen_cuatrimestre`: importe y margen por cuatrimestre (1: ene-abr, 2: may-ago, 3: sep-dic).
  - `margen_por_sucursal`, `importe_por_sucursal`.
  - `top_clientes_margen`, `top_vendedores_margen` (top 10).
  - `margen_por_linea`.
  - Totales: `importe_total`, `ganancia_bruta`, `kilos_vendidos`.
    Devuelve un objeto validado por `respuesta_total`.
- **`Ia_Service`** ([app/services/ia_service.py](app/services/ia_service.py)): Cliente Groq para generar recomendaciones a partir del JSON de resultado. Para activarlo configure la variable `GROQ_API_KEY` en el entorno. Si no está disponible, la generación de recomendación está comentada por defecto.

**Schema de respuesta**

- Ver [app/schemas/response_schema.py](app/schemas/response_schema.py). Campos principales:
  - `importe_margen_cuatrimestre`: lista con `{CUATRIMESTRE, IMPORTE_TOTAL, MARGEN_TOTAL}`
  - `margen_por_sucursal`, `importe_por_sucursal`: listas por `nombre_sucursal` con totales.
  - `top_clientes_margen`, `top_vendedores_margen`: listas con `MARGEN_TOTAL`.
  - `margen_por_linea`: lista por `nombre_linea`.
  - `importe_total`, `ganancia_bruta`, `kilos_vendidos`: totales numéricos.
  - `recomendacion`: texto opcional generado por IA.

**Configuración y CORS**

- Orígenes permitidos en [app/core/config.py](app/core/config.py). Ajustar `ORIGINS` si el frontend se sirve desde otra URL.

**Tests**

- Ejecutar tests con `pytest` desde la raíz del proyecto:

```
pytest -q
```

- Los tests usan fixtures en `tests/fixtures/` y cubren:
  - Validación de lectura de archivos (`tests/unit/test_validacion_service.py`).
  - Cálculos y eliminación de duplicados (`tests/unit/test_procesar_service.py`).

**Notas y recomendaciones**

- Para habilitar recomendaciones IA, exportar la variable de entorno `GROQ_API_KEY` (por ejemplo en Windows PowerShell):

```
$env:GROQ_API_KEY = "tu_api_key"
```

- Mantener `requirements.txt` actualizado con `pip freeze > requirements.txt` antes de push.

---
