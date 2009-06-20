
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
    #@param words: Mapeamento de palavras 
    def __init__(self, words):
        self.words = words
    #@param input: Lista de palavras    
    def process(self, input):
        for old_word in input:
            if old_word in self.words:
                yield self.words[old_word]
            else:
                yield old_word

class InputFiltro(Filtro):
    def __init__(self, msg = ''):
        self.msg = msg
    
    def process(self, input):
        result = raw_input(self.msg)
        return result
        

class OutputFiltro(Filtro):
    def process(self, input):
        print input
        return input
    

class ConstantFiltro(Filtro):
    def __init__(self, val):
        self.val = val
        
    def process(self, input):
        return self.val

