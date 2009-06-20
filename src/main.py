from pipes import *
from filters import *
from decorators import *
from pipes_filters import *


if __name__ == '__main__':
    
    f = TuboSequencial(
                                             
           TuboParalelo(
              ConstantFiltro(["abc", "def", "fgh"]),
              ReplaceFiltro({"abc":"123", "def":"456", "fgh":"789"})
           ),
           
           Base64EncodeFiltro(),
           
           JoinDecorator(
              Base64DecodeFiltro()
           ),
           
           OutputFiltro()
           
    )

    go(f)
