import matplotlib.pyplot as plt

def plotar_grafico(x, y,labely,labelx,color='blue'):
    
    plt.scatter(x, y, color=color, label='Pontos de dados')
    
    
    plt.title("Gráfico de Dispersão")
    plt.xlabel(labelx)
    plt.ylabel(labely)
    
    
    plt.legend()
    
    
    plt.show()

def plotar_grafico_com_estimador(x, y, estimador,labely, labelx, color='blue'):
    
    plt.scatter(x, y, color=color, label='Pontos de dados')
    
    
    y_estimado = [estimador(i) for i in x]
    
    
    plt.plot(x, y_estimado, color='red', label='Linha de Estimativa', linewidth=2)
    
    
    plt.title("Gráfico de Dispersão com Linha de Estimativa")
    plt.xlabel(labelx)
    plt.ylabel(labely)
    
    
    plt.legend()
    
    
    plt.show()