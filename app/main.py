from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import procesar_controller

app = FastAPI()

# Configuracion del cors
origins = [
    "http://localhost:3000",  # frontend en el localhost)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Aqui van registrando los controllers (routers por que aqui los llaman asi (?)) creados, 
# seguir la mimsa estructura cada que se quiera crear un nuevo controlador
app.include_router(procesar_controller.router)