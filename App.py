'''
Are You Banned?

Con este 'programa' (jejejeje) podras saber si tu URL (sitio web)
esta o no banneado por Google, y por eso espero que sepas que si
estas banneado no podras participar en los servicios de Google
Adsense y no se cuantos otros.


Autor: David256
'''
import aybm

ay = aybm.ayb()



print("Are You Banned - by David256")
print("")

url = input("Escribe la URL: ")
info = ay.enviar(url)
estado = ay.extraerEstado(info)
print(info)
