from pipes_filters import Tubo

from processing import Process, Queue


class TuboSequencial(Tubo):
    def __init__(self, *filters):
        self.filters = filters
    
    def process(self, input):
        output = input
        
        for filter in self.filters:
            output = filter.process(output)
        
        return output


class TuboParalelo(Tubo):
    def process(self, input):
        
        def procProdutor(filtroA, inputA, queue):
            for result in filtroA.process(inputA):
                queue.put(result)
                
            queue.put(None)
        
        def procConsumidor(filtroB, in_queue, out_queue):
            input = in_queue.get()
            
            while input is not None:
                result = filtroB.process(input)
                out_queue.put(result)
                
                input = in_queue.get()
                
            out_queue.put(None)
        
        AtoB_queue = Queue()
        BtoC_queue = Queue()
        
        procA = Process(
            target = procProdutor,
            args = (self.filtroA, input, AtoB_queue)
        )
        
        procB = Process(
            target = procConsumidor,
            args = (self.filtroB, AtoB_queue, BtoC_queue)
        )
        
        procA.start()
        procB.start()
        
        res = BtoC_queue.get()
        while res is not None:
            yield res
            res = BtoC_queue.get()

        procA.join()
        procB.join()
