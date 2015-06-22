#Version: Python 3.4.4

import urllib.request
import sys


class ayb():

    def __init__(self):
        self.HOST = 'http://isbanned.com'

    def enviar(self, unaUrl):
        #envia la peticion a la web
        #   unaUrl debe ser byte
        datos = b'url=' + unaUrl + b'&4rme=Submit'
        urr = urllib.request.Request(self.HOST + '/index.php', datos)
        uru = urllib.request.urlopen(urr)
        return uru.read(4096).decode('utf-8')

    def extraerEstado(self, fuente):
        inbuscar = 'id="myText" value="'
        fibuscar = '">'
        if fuente.find(inbuscar)!=-1 and fuente.find(fibuscar)!=-1:
            pseudoInicio = fuente.find(inbuscar)
            inicio = int(pseudoInicio) + len(inbuscar)
            fin = fuente.find(fibuscar)
            estado = fuente[inicio,fin]
            return estado
        else:
            return False
