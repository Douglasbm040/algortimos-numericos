def gerar_transposta(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    matriz_transposta = []
    
    for coluna in range(colunas):
        linha_transposta = []
        for linha in range(linhas):
            linha_transposta.append(matriz[linha][coluna])
        matriz_transposta.append(linha_transposta) 
         
    return matriz_transposta

def transformar_matriz_para_nx2(matriz):
    elementos = [item for linha in matriz for item in linha]
    
    matriz_nx2 = [elementos[i:i+2] for i in range(0, len(elementos), 2)]
    
    return matriz_nx2

        
  
def get_column(matriz, pos_coluna):
    return [linha[pos_coluna] for linha in matriz]

def get_row(matriz, pos_linha):
    return matriz[pos_linha]



def gerar_matriz_confusao(falso_positivo, falso_negativo, verdadeiro_positivo, verdadeiro_negativo):
   return [
        [verdadeiro_negativo, falso_positivo],  
        [falso_negativo, verdadeiro_positivo]   
    ]