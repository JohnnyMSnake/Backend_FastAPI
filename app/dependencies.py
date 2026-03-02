from .services.validacion_service import Validacion_Service

#Aqui se registran todos los services para que puedan ser inyectados
def Validacion():
    return Validacion_Service()