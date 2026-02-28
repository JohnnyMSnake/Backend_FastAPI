1.-
Si es la primera vez que jalas el repositorio, siempre crea tu venv:
===========================================================================
python -m venv venv
===========================================================================

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


2.-
Cada que jalen el repositorio, siempre ejecuten el siguiente comando:
===========================================================================
pip install -r requirements.txt
===========================================================================
Esta madre lo que hace es instalarles todos los modulos que sean neecsarios para trabajar o 
les terminara tirando un error de modulos.


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

3.-
Al igual que el anterior, antes de hacer push al repositorio remoto, SIEMPRE HAGAN ESTE COMANDO ANTES DE:
===========================================================================
pip freeze > requirements.txt
===========================================================================
Esta madre indicara en el requirements.txt todos los modulos que se hayan instalados, aydua a que el punto
anterior tenga funcione correctamente y todos sean felices sin errores UwU.