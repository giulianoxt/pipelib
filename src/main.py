from pipes import *
from filters import *
from decorators import *
from pipes_filters import *


if __name__ == '__main__':
    f = TuboSequencial(InputFiltro(), OutputFiltro())

    go(f)
