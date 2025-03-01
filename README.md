# Estimador de Carbono-14

Este projeto visa fornecer um modelo para estimar as amostras de Carbono-14, incluindo os métodos para calcular os parâmetros `beta0` e `beta1`. A arquitetura foi projetada para facilitar a manipulação e visualização dos dados, além de integrar a extração de tabelas de PDFs.

## Arquitetura do Projeto

O projeto é organizado de forma modular, utilizando uma estrutura comum em projetos de Ciência de Dados. A seguir, apresentamos a divisão das pastas e o que cada uma contém:

### `models/`
Contém o modelo de estimativa de Carbono-14 e os métodos para calcular `beta0` e `beta1`, essenciais para a previsão. Os métodos também incluem as estratégias usadas na função `fit` do modelo.

- **C14_ESTIMADOR_MODEL.py**: Implementação do modelo de estimativa de Carbono-14.
- **metodos/MMQ.py**: Métodos para calcular os parâmetros `beta0` e `beta1` com a técnica dos Mínimos Quadrados (MMQ).
- **metodos/STRATEGYS.py**: Estratégias utilizadas na função `fit` do modelo para estimativas.

### `service/`
Responsável pelas manipulações matemáticas e matriciais. As funções dessa pasta são essenciais para realizar operações como multiplicação, inversão e outras operações matriciais.

- **algebra_service.py**: Funções responsáveis pela manipulação e operação em matrizes.

### `utils/`
Contém funções auxiliares para tarefas diversas, como a leitura e extração de dados de arquivos PDF, bem como outras funções utilitárias para manipulação de dados.

- **pdf_util.py**: Funções para abrir um arquivo PDF e extrair a tabela da página 2.

### `view/`
Responsável pela criação de gráficos e visualizações dos dados e resultados. Utiliza a biblioteca `matplotlib`.

- **DISPERSAO.py**: Responsável pela visualização gráfica de dispersão dos resultados.

### `main.py`
Arquivo principal do projeto. Ele orquestra a execução do código, realizando a carga dos dados, passando pelos modelos de estimativa e finalizando com a visualização dos resultados.

---

## Como Usar

### Passo 1: Instalar as Dependências

Para instalar as dependências necessárias, execute o seguinte comando no seu terminal:

```bash
pip install pdfplumber matplotlib

