
class Filtro(object):
    """
        Filtro identidade
    """
    
    def process(self, input):
        return input


class Tubo(Filtro):
    def __init__(self, filtroA, filtroB):
        self.filtroA = filtroA
        self.filtroB = filtroB

    def process(self, input):
        """ Implementar nas classes base """
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


class TuboSequencial(Tubo):
    def process(self, input):
        outA = self.filtroA.process(input)
        outB = self.filtroB.process(outA)
        
        return outB


