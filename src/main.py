from pipes import *
from filters import *
from decorators import *
from pipes_filters import *


if __name__ == '__main__':
    
    f = TuboSequencial(
                       
            TuboSequencial(
                InputFiltro(),
                Base64EncodeFiltro()
            ),
            
            OutputFiltro()
    )

    go(f)
