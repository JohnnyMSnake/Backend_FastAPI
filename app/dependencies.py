from app.services.procesar_service import Procesar_service
from app.services.validacion_service import Validacion_Service

#Aqui se registran todos los services para que puedan ser inyectados
def Validacion():
    return Validacion_Service()

def Procesar():
    return Procesar_service()