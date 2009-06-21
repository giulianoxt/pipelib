
class Filtro(object):
    """
        Filtro identidade
    """
    
    def process(self, input):
        return input


class Tubo(Filtro):
    def __init__(self, *filtros):
        self.filtros = filtros

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
        output = self.filtro.process(input)
        return output


def run(filtro, first_input = None):
    filtro.process(first_input)
