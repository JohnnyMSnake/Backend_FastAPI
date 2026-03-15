from fastapi import FastAPI

from app.core.cors import ConfigCors

from .routers import procesar_controller

app = FastAPI()

# Configuracion del cors
ConfigCors(app)

#Aqui van registrando los controllers (routers por que aqui los llaman asi (?)) creados, 
# seguir la mimsa estructura cada que se quiera crear un nuevo controlador
app.include_router(procesar_controller.router)