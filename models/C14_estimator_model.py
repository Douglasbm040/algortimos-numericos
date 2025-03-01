from models.metodos.Strategy.metodo_strategy import MetodoStrategy
from service.algebra_service import gerar_matriz_confusao
 
import math

class C14EstimatorModel:
    def __init__(self,n:list,t:list):
        self.x=0
        self.n = n
        self.beta_0 = 0
        self.beta_1 = 0
        self.e = math.e
        self.t = t

    def predict(self, N):
        return self.beta_0 + self.beta_1 * N

    
    def score(self,xteste,yteste,erro_tolerancia=10):  
        y_estimado = [self.predict(i) for i in xteste]
        acuracia = self.__acuracia(yteste,y_estimado,erro_tolerancia)
        return acuracia
    
    
    def __acuracia(self, y: list, yprevisto: list,tolerancia) -> float:
        
        if len(y) != len(yprevisto):
            raise ValueError("As listas y e yprevisto devem ter o mesmo tamanho.")
        
        acuracia = sum(1 for real, previsto in zip(y, yprevisto) if abs(real - previsto) <= tolerancia)
        acuracia_percentual = (acuracia / len(y)) * 100
        
        return acuracia_percentual
            
    def fit(self,metodo:MetodoStrategy):
        self.beta_0, self.beta_1 = metodo.executar(self.n, self.t)
