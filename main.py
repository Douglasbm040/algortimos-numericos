from utils import arq_util, pdf_util 
from service import algebra_service

from models.metodos.MMQ import MMQ
from models.C14_estimator_model import C14EstimatorModel
from view import dispersao_plot

arq_pdf = r"data/raw/Trabalho-2.pdf"

#preprocessamento
pdf = pdf_util.open_pdf(arq_pdf)
matriz,vetor_cabecalho = pdf_util.extrair_tabela(pdf)
matriz = algebra_service.gerar_transposta(matriz)
matriz = algebra_service.transformar_matriz_para_nx2(matriz)

y = [linha[0] for linha in matriz]  
x = [linha[1] for linha in matriz]
### visualização de dados
dispersao_plot.plotar_grafico(x,y,labelx='quantidade de caborno 14 na amostra',labely='tempo em anos')

##validação do modelo de estimativa 
porcentagem_validacao = 0.8
Xtreino, ytreino, xteste, yteste = x[:int(len(x)*porcentagem_validacao)], y[:int(len(x)*porcentagem_validacao)], x[int(len(x)*porcentagem_validacao):], y[int(len(x)*porcentagem_validacao):]
modelo_validacao = C14EstimatorModel(Xtreino,ytreino)
modelo_validacao.fit(MMQ())
acuracia= modelo_validacao.score(xteste,yteste,erro_tolerancia=100)
print('acuracia: %.2f %%' % acuracia)

##crição do modelo de estimativa
modelo = C14EstimatorModel(x,y)
###ajuste da curva
modelo.fit(MMQ())
###previsão
dispersao_plot.plotar_grafico_com_estimador(x,y,estimador=modelo.predict,color='red',labelx='quantidade de caborno 14 na amostra',labely='tempo em anos')

#respondendo a pergunta :
print('valor em anos eh: ',modelo.predict(53307321157))