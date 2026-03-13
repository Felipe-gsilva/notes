---
lang: pt-BR
---

# A era dos dados
A cada 20 meses, a quantidade de dados armazenados no mundo dobra.

Dados podem ser estruturados, não-estruturados ou semi estruturados.

Tabelas de atributos: objetos do mundo físico são abstraídos e representados como um conjunto de atributos.

Variável pode ser: 
- quantitativa
    - discreta 
    - continua
- qualitativa
    - nominal 
    - ordinal

Escala dos dados: define as operações permitidas sobre os valores dos atributos 

## Dados qualitativos
Escala nominal: não conseguimos ordenar (apenas == e !=)
- ex: 'id', cor, sexo

Escala ordinal: podemos ordenar (ops: ==, !=, >, <, >=, <=)

## Dados Quantitativos
Escala Intervalar 
Escala racional

# Análise e Exploração dos dados (AED)

1. Estatística descritiva:
- medidas de localidade 
- espalhamento e distribuição...

2. Visualização
- Gráficos de Barras, dispersão, boxplots
- Técnicas de visualização específicas (ilustração com grafos, *treemaps*, *stacked maps*, KDE, PCA) 

resto da aula foi código

# Pré-processamento de dados

Técnicas usadas para melhorar a qualidade dos dados.
Eliminam ou minimizam problemas como ruídos ou presença de *outliers*:

- Remoção de atributos: podemos remover dados irrelevantes para o problema, quando, por exemplo, dada coluna não tem correlação alguma com o objetivo do modelo.
- Integração de dados: *merge* de *datasets*.
- Amostragem de dados: algoritmos de *machine learning* podem ter dificuldades em lidar com quantidades abundantes de objetos: trade-off (balanceamento entre eficiencia computacional x acurácia - taxa de predições corretas)
    - A amostragem deve ser representativa.
    - Diferentes processos de amostragem alteram grandemente os resultados.
    - A amostragem pode ser: 
        - Aleatória simples
        - Estratificada: usada quando as classes apresentam propriedades distintas (proporcional as classes do problema).
        - Progressiva: progressivamente crescer o tamanho da amostra.
- Balanceamento de dados
- limpeza de dados/remoção de *outliers*
    - podemos ter dados com ruído (possuir valor distinto do esperado) ou inconsistência.
    - Estratégias de valores ausentes
        - Eliminar a coluna inteira 
        - preencher artesanalmente 
        - implicar algum algoritmo de ML ou heurística para preencher os campos
    - Estratégias de dados redundantes 
        - Eliminar colunas redundantes 
        - Agrupar os registros em um só 
        - Empregar algoritmos de agrupemento (k-means ou DBSCAN).
        - Usar técnicas de redução de dimensionalidade, mantendo apenas os componentes com maior variação.
        - Uso de Feature Selection (ex: random forest, LASSO).
- transformação de dados
    - label encoding: converte dados qualitativos em quantitativos, cada categoria pode ser passada para um número. (i.e. febre (alta, baixa) (1, 0))
    - one hot encoding: converter dados qualitativos (nominais/outros) em formato adequado. Cria colunas binárias separadas para cada categoria única. Variável de flag.
    - tecnicas de reescalonamento: converter atributos para uma escala adequada. Tenta normalizar as variáveis entre si.
        - Escalonamento via mediana + IQR -> menos usados
        - Padronização: $X_{stand} = \frac{X - mean(X)}{std(X)}$ - std = desvio-padrão
        - Normalização min-max: $X_{norm} = \frac{X - X_{min}{X_{max} - X_{min}}}$

