from pipes_filters import Tubo

from Queue import Queue
from threading import Thread


class TuboSequencial(Tubo):
    def __init__(self, *filters):
        self.filters = filters
    
    def process(self, input):
        output = input
        
        for filter in self.filters:
            output = filter.process(output)
        
        return output


class TuboParalelo(Tubo):
    def __init__(self, *filtros):
        self.filtros = filtros
    
    def process(self, input):
        
        def queueToGenerator(queue):
            obj = queue.get() if queue else None
            
            while obj is not None:
                yield obj
                obj = queue.get()

        def generatorToQueue(gen, queue):
            for obj in gen:
                queue.put(obj)
            
            queue.put(None)

        def threadFiltro(filtro, in_queue, out_queue):
            if in_queue is None:
                outputGen = filtro.process(input)
            else:
                inputGen  = queueToGenerator(in_queue) 
                outputGen = filtro.process(inputGen)
            
            generatorToQueue(outputGen, out_queue)
        
        
        threads, queue = [], None
        
        for filtro in self.filtros:
            new_queue = Queue()
     
            t = Thread(
                target = threadFiltro
              , args   = (filtro, queue, new_queue)
            )
            
            queue = new_queue
            t.start()
            threads.append(t)
            
        for result in queueToGenerator(queue):
            yield result
        
        for t in threads:
            t.join()

