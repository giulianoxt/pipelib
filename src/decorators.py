from pipes_filters import Decorator
import string

class JoinDecorator(Decorator):
    """
        Transforma um filtro que gera
        um resultado em pedacos (generator)
        em um filtro que gera um resultado unico.
        
        O resultado unico vai ser uma lista
    """
    def process(self, input):
        generator = Decorator.process(self, input)
        
        result = list(generator)
        return result


class SplitDecorator(Decorator):
    """
        Transforma um filtro que gera
        uma lista, em um filtro
        que retorna um generator.
        
        Assim, o filtro resultante podera ser
        utilizado no TuboParalelo
    """
    
    def process(self, input):
        result_list = Decorator.process(self, input)
        
        for result in result_list:
            yield result


class SplitStringDecorator(Decorator):    
    def process(self, input):
        res = string.split(Decorator.process(self, input), " ")
        for x in res:
            yield x

