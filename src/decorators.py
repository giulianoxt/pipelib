from pipes_filters import Decorator

class JoinDecorator(Decorator):
    """
        Transforma um filtro que gera
        um resultado em pedaços (generator)
        em um filtro que gera um resultado único.
        O resultado único vai ser uma lista
    """
    def process(self, input):
        generator = super(self).process(input)
        
        result = list(generator)
        return result
