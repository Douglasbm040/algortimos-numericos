Estimador de Carbono-14
Este projeto visa fornecer um modelo para estimar as amostras de Carbono-14, incluindo os métodos para calcular os parâmetros beta0 e beta1. A arquitetura foi projetada para facilitar a manipulação e visualização dos dados, além de integrar a extração de tabelas de PDFs.

Arquitetura do Projeto
O projeto é organizado de forma modular, utilizando uma estrutura comum em projetos de Ciência de Dados. A seguir, apresentamos a divisão das pastas e o que cada uma contém:

carbono14-estimador/
├── models/
│ ├── C14_ESTIMADOR_MODEL.py # Modelo para estimativa de amostras de Carbono-14
│ ├── metodos/
│ │ ├── MMQ.py # Métodos para calcular beta0 e beta1
│ │ └── STRATEGYS.py # Estratégias para a função fit do modelo
├── service/
│ └── algebra_service.py # Funções de manipulação matricial
├── utils/ # Funções auxiliares gerais
│ ├── pdf_util.py # Função para abrir e extrair a tabela do PDF
|
├── view/
│ └── DISPERSAO.py # Visualização dos resultados e gráficos
├── main.py # Arquivo principal para execução do código
├── requirements.txt # Dependências do projeto
└── README.md # Este arquivo
Descrição das Pastas
models/: Contém o modelo de estimativa de Carbono-14 e os métodos para calcular beta0 e beta1, essenciais para a previsão. Os métodos também incluem estratégias que são usadas na função fit do modelo.

service/: Responsável pelas manipulações matemáticas e matriciais. A principal função desta pasta é realizar operações matriciais complexas, como multiplicação e inversão, essenciais para o modelo de estimativa.

utils/: Contém funções auxiliares para tarefas diversas, como a leitura e extração de dados de arquivos PDF, bem como outras funções utilitárias para manipulação de dados.

view/: Onde as visualizações dos resultados são geradas. Utiliza a biblioteca matplotlib para criar gráficos e facilitar a análise visual dos dados.

main.py: Arquivo de entrada principal do projeto. Orquestra a execução, carregando os dados, passando pelo modelo de estimativa e finalizando com a visualização dos resultados.
