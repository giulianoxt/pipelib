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

