# Proyecto Backend - Procesamiento de datos comerciales

API construida con FastAPI para cargar archivos de ventas en formato CSV o XLSX, validarlos, normalizar la información y generar indicadores de negocio listos para consumo por un frontend o por herramientas de análisis.

La API procesa datos como importe, margen, kilos vendidos, sucursal, cliente, vendedor y línea. A partir de eso calcula totales, agrupaciones por cuatrimestre, sucursal, cliente, vendedor y línea, además de exponer una estructura de respuesta validada con Pydantic. El proyecto también contempla una integración opcional con IA para generar recomendaciones a partir del resumen calculado.

## Qué hace el proyecto

- Recibe archivos cargados por el usuario mediante un endpoint REST.
- Valida que el formato sea compatible (`.csv` o `.xlsx`).
- Normaliza datos para reducir errores de captura y duplicados.
- Calcula métricas de negocio como importe total, ganancia bruta y kilos vendidos.
- Genera rankings y agregaciones por cuatrimestre, sucursal, cliente, vendedor y línea.
- Expone una respuesta estructurada para consumirla desde frontend o desde Swagger.

## Estructura general

- `app/main.py`: punto de entrada de FastAPI.
- `app/routers/`: rutas HTTP del backend.
- `app/services/`: lógica de validación, procesamiento e integración con IA.
- `app/schemas/`: modelos Pydantic de la respuesta.
- `app/core/`: configuración general, CORS y variables de entorno.
- `tests/`: pruebas unitarias del flujo principal.
- `recursos/`: archivos de ejemplo o base de datos de apoyo.

## Requisitos previos

- Python instalado en la misma versión que se use para crear el entorno virtual.
- Un entorno virtual aislado para evitar conflictos de dependencias.
- Acceso a Internet solo si vas a instalar dependencias o usar la integración con IA.

## Instalación

1. Crear el entorno virtual:

```bash
python -m venv venv
```

2. Activar el entorno virtual en Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Cómo correr el proyecto

Levanta la API en modo desarrollo con:

```bash
uvicorn app.main:app --reload
```

Una vez encendido el servidor, puedes abrir la documentación interactiva de FastAPI en:

```text
http://127.0.0.1:8000/docs
```

## Endpoints principales

- `GET /procesar/`: endpoint de prueba para verificar que la ruta está activa.
- `POST /procesar/`: recibe un archivo y devuelve el resumen calculado.

El archivo debe venir como subida tipo `multipart/form-data` en el campo `file`.

## Pruebas

El proyecto incluye pruebas unitarias para validar el procesamiento y la validación de archivos.

Ejecuta las pruebas con:

```bash
pytest
```

## Cómo evitar problemas con versiones y requirements

- Usa siempre un entorno virtual nuevo por proyecto; no instales dependencias globalmente.
- Antes de ejecutar o compartir el proyecto, corre `pip install -r requirements.txt` para asegurar que todos usen las mismas librerías.
- Si agregas, quitas o actualizas paquetes, regenera el archivo de dependencias con:

```bash
pip freeze > requirements.txt
```

- Mantén alineada la versión de Python entre desarrollo local, pruebas y despliegue.
- Si aparece un error raro de dependencias, borra y recrea el entorno virtual, luego reinstala desde `requirements.txt`.
- Si vas a usar la recomendación por IA, define la variable de entorno `GROQ_API_KEY` en un archivo `.env` o en el entorno del sistema.

## Flujo de procesamiento

1. El archivo llega al endpoint `POST /procesar/`.
2. El servicio de validación detecta si es CSV o XLSX.
3. La información se carga en un DataFrame de pandas.
4. Se eliminan duplicados y se normalizan valores vacíos y texto.
5. Se calculan agregaciones y totales de negocio.
6. Se devuelve una respuesta tipada y lista para consumo.

## Valor del proyecto

Este backend muestra experiencia en:

- Construcción de APIs con FastAPI.
- Manejo de archivos y limpieza de datos con pandas.
- Diseño de respuestas tipadas con Pydantic.
- Pruebas unitarias para validación y procesamiento.
- Integración opcional con IA para análisis y recomendaciones.
- Organización del código por capas para facilitar mantenimiento y escalabilidad.

## Notas técnicas

- La API permite archivos CSV con distintas codificaciones comunes.
- El procesamiento considera fechas con formato día/mes para evitar errores de interpretación.
- La documentación automática de FastAPI facilita probar la API sin Postman.
- El CORS se controla por entorno con `CORS_ORIGINS` y, si hace falta, `CORS_ALLOW_ORIGIN_REGEX`; en producción el `Origin` debe coincidir exactamente con uno permitido.

## Comandos rápidos

```bash
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
pytest
```
