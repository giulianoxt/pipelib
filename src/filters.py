
from pipes_filters import *
from base64 import *
from zlib import *
from string import *


class Base64EncodeFiltro(Filtro):
    def process(self, input):
        return b64encode(input)

        
class Base64DecodeFiltro(Filtro):
    def process(self, input):
        return b64decode(input)

    
class CompressFiltro(Filtro):
    def process(self, input):
        return compress(input)

    
class DescompressFiltro(Filtro):
    def process(self, input):
        return decompress(input)

    
class ReplaceFiltro(Filtro):
    def __init__(self, words):
        self.words = words
        
    def process(self, input):
        res = input
        for key in iter(self.words):
            res = replace(key, self.words[key], res)
        return res


class InputFiltro(Filtro):
    def __init__(self, msg = ''):
        self.msg = msg
    
    def process(self, input):
        result = raw_input(self.msg)
        return result
        

class OutputFiltro(Filtro):
    def process(self, input):
        print input
        return None

