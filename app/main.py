from fastapi import FastAPI
from .controllers import procesar_controller

app = FastAPI()

#Aqui van registrando los controllers creados, seguir la mimsa estructura cada que se queira crear 
#un nuevo controlador
app.include_router(procesar_controller.router)