class Filtro(object):
    def process(self, input):
        # Implementar nas classes base
        raise NotImplementedError


class Tubo(Filtro):
    def __init__(self, filtroA, filtroB):
        self.filtroA = filtroA
        self.filtroB = filtroB

    def process(self, input):
        # Implementar nas classes base
        raise NotImplementedError


class Decorator(Filtro):
    """
        Decorator identidade, nao altera nada
        do filtro passado
    """
    
    def __init__(self, filtro):
        self.filtro = filtro
    
    def process(self, input):
        self.filtro.process(input)

