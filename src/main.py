from pipes import *
from filters import *
from decorators import *
from pipes_filters import *


if __name__ == '__main__':
    
    f = TuboSequencial(
                                             
           TuboParalelo(
              ConstantFiltro(["abc", "def", "ghi"]),
              
              ReplaceFiltro({"abc":"123", "def":"456", "ghi":"789"}),
              
              Base64EncodeFiltro(),
              
              Base64DecodeFiltro(),
              
              ReplaceFiltro({"123":"abc", "456":"def", "789":"ghi"})
           ),

           MapFiltro(lambda l : ''.join(l)),
           
           OutputFiltro()
           
    )

    go(f)
