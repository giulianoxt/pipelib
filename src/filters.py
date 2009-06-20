
from pipes_filters import *
from base64 import *
from zlib import *

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