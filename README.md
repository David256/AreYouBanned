# AreYouBanned
Permite conocer si tu sitio web esta banneado por Google usando de una forma no tradicional el servicio de IsBanned.com
Este es un conjunto de script python que incluye un par de funciones que permite lograr el objetivo

# Libreria
Incluye la libreria aybm (AreYouBannedModule), que incluye dos funciones:

## Enviar(unaURL)
Esta función es la encargada de enviar la petición al servidor y retornar el código html que recibe.

## extraerEstado(fuente)
Esta función se encarga de buscar lo que necesitamos: busca el resultado devuelto por el servidor, que informa si la url
pasada como aprametro en la función Enviar() esta banneada por Google o no lo esta.

# App.py
El script de App implementa este módulo aybm. Además da un claro ejemplo de como se debe usar.
