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


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


4.-
Para poder levantar la API, solo ejecuten el siguiente comando:
===========================================================================
uvicorn app.main:app --reload
===========================================================================
Los podnra en modod desarrollador y cada que hagan modfiicaciones y guarden, se reflejara al toque los cambios 
que hayan realizado.


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


5.- 
Se que algunos no tienen idea, pero FastAPI ya crea una documentaciond e las APIs creadas de manera automatica y se 
peude testear sin necesidad de usar postman (Esta madre se llama Swagger) por lo que les facilitara el testeo de 
la API. para acceder es solo meterse a la siguiente URL:
==========================================================================
http://127.0.0.1:8000/docs
==========================================================================
Es bastante intuitivo de usar, en caso de que no entiendan que carajos, preguntenle a GPT como se usa.
