from models.metodos.Strategy.metodo_strategy import MetodoStrategy
import math

class MMQ(MetodoStrategy):
    #@abstractmethod
    def executar(self, x:list, y:list): 
        return  self.__get_intercepto(x,y), self.__get_coeficiente_angular(x,y)
    def __somatorio_vetor(self,vetor:list):
        return sum(vetor)
    
    def __somatorio_quadrado_vetor(self,vetor:list):
        return sum(math.pow(i,2) for i in vetor)
    
    def __somatorio_produto_vetor(self,vetorY:list,vetorX:list):
        if len(vetorY) == len(vetorX):
            return sum(vetorX[pos]* vetorY[pos] for pos in range(len(vetorY)))
        else:
            raise ValueError("Os vetores devem ter o mesmo tamanho.")
        
    def __get_coeficiente_angular(self, x:list, y:list):
        numerador = (len(x) * self.__somatorio_produto_vetor(x,y)) - (self.__somatorio_vetor(x)*self.__somatorio_vetor(y))
        denominador = (len(x) * self.__somatorio_quadrado_vetor(x)) - (self.__somatorio_vetor(x)**2)
        if denominador == 0:
            raise ValueError("operação invalidar denominador igual a zero.")
        return numerador/denominador

    
    def __get_intercepto(self, x:list, y:list):
        numerador = self.__somatorio_vetor(y) - self.__get_coeficiente_angular(x,y) * self.__somatorio_vetor(x)
        denominador = len(x)
        if denominador == 0:
            raise ValueError("operação invalidar denominador igual a zero.")
        return numerador/denominador