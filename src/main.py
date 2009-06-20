from pipes import *
from filters import *
from decorators import *
from pipes_filters import *


if __name__ == '__main__':
    
    f = TuboSequencial(
                       
           TuboSequencial(
        
                ConstantFiltro(["abc", "def", "fgh"]),
                
                JoinDecorator(
                    ReplaceFiltro({"abc":"123", "def":"456", "fgh":"789"})
                )
                
           ),
           
           OutputFiltro()
                       
    )

    go(f)
