from fastapi import FastAPI
from .routers import procesar_controller

app = FastAPI()

#Aqui van registrando los controllers (routers por que aqui los llaman asi (?)) creados, 
# seguir la mimsa estructura cada que se quiera crear un nuevo controlador
app.include_router(procesar_controller.router)