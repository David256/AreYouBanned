#Version: Python 3.4.4

import urllib.request
import sys


class ayb():

    def __init__(self):
        self.HOST = 'isbanned.com'

    def enviar(self, unaUrl):
        #envia la peticion a la web
        #   unaUrl debe ser byte
        datos = b'url=' + unaUrl + b'&4rme=Submit'
        urr = urllib.request.Request(self.HOST + '/index.php', datos)
        uru = urllib.request.urlopen(urr)
        return uru.read(2048).decode('utf-8')
