import pdfplumber

def open_pdf(path) -> pdfplumber.pdf.PDF:
    pdf = pdfplumber.open(path)
    return pdf

def extrair_tabela(pdf: pdfplumber.pdf.PDF):
    matriz = []
    table_pdf = pdf.pages[1].extract_table()
    cabecalho_tabela = table_pdf[0]
    
    for coluna in table_pdf[1]:
        matriz.append([int(numero) for numero in coluna.split('\n')])
    return (matriz,cabecalho_tabela)