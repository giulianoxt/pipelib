from pipes_filters import Tubo

class TuboSequencial(Tubo):
    def process(self, input):
        outA = self.filtroA.process(input)
        outB = self.filtroB.process(outA)
        
        return outB
