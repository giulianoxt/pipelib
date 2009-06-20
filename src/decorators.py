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


class SplitDecorator(Decorator):
    """
        Transforma um filtro que gera
        uma lista, e transforma em um filtro
        que retorna um generator.
        
        Assim, o filtro resultante poderá ser
        utilizado no TuboParalelo
    """
    
    def process(self, input):
        result_list = super(self).process(input)
        
        for result in result_list:
            yield result
