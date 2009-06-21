
from pipes_filters import *
from base64 import *
from zlib import *
from string import *


class Base64EncodeFiltro(Filtro):
    #@param input: Lista de palavras
    def process(self, input):
        for x in input:
            yield b64encode(x)

        
class Base64DecodeFiltro(Filtro):
    #@param input: Lista de palavras
    def process(self, input):
        for x in input:
            yield b64decode(x)

    
class CompressFiltro(Filtro):
    #@param input: Lista de palavras 
    def process(self, input):
        objcomp = compressobj()
        for word in input:
            yield objcomp.compress(word)
        yield objcomp.flush(Z_FINISH)

    
class DecompressFiltro(Filtro):
    #@param input: Lista de palavras
    def process(self, input):
        objdecomp = decompressobj()
        for word in input:
            yield objdecomp.decompress(word)
        yield objdecomp.flush()

    
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

