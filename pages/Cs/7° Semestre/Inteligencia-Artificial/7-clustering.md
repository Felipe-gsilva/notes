# Agrupamento de Dados
Ideia abstrata de cluster: Coleção de objetos próximos no espaço de atributos.

> [!ATTENTION] Um desafio deste tipo de problema é ser completamente assertivo em relação ao número de clusters.

## Definições Básicas 

1. Um cluster bem divido é aquele com grupos com similaridade maior entre si do que em relação à outro cluster.
2. Cluster baseado no centro: grupo de objetos tal que qualquer objeto em um dado cluster está mais próximo (ou é mais similar ) ao centro do referido cluster (chamado de centroide, temos a média aritmética entre todos os membros do cluster).
3. Cluster continuo: os dados estão mais próximos entre outros clusters.
4. Cluster hierárquico: grupo de objetos onde há uma hierarquia definida entre seus objetos.

## Aspectos importantes 
1. Ajuste de parâmetros: por exemplo, o número de clusters.
2. Há a possibilidade de que mais de uma estrutura relevante exista nos dados.


## Etapas de análise de agrupamento
1. Preparação dos dados
- Conversão de tipos de dados.
- Normalizar os dados.
- Redução do número de atributos, com seleção ou diminuição de dimensionalidade.
2. Calcular proximidade entre objetos usando EDs
- Matriz de Similaridade
- Grafo de similaridade

### Matriz de Similaridade
Similaridade entre cada par de atributos. 
Cada elemento da matriz X(i, j) é dado por um cálculo de de distância entre o objeto $x_i$ e $x_j$.

Podemos medir:
1. Proximidade entre objetos.
2. Proximidade entre objeto e clusters.
3. Proximidade entre dois clusters.


### Métricas de distância
1. Medida de dissimilaridade: $d(x_i, x_j)$ é máxima.
    - Ex: distância euclidiana.
    - $d(x, y) \geq 0, \forall x,y$ 
    - $d(x, y) = d(y, x), \forall x,y$ 
    - $d(x, z) \leq d(x, y) + d(y, z), \forall x,y \text{e} z$ 

2. Medida de similaridade: d($x$ , $y$) = 1.
    - Ex: correlação
    - $s(x,y) = 1$  (ou o valor máximo) é o melhor caso. $0 \leq s(x,y) \leq 1$
    - $s(x, y) = s(y, x), \forall x, y$

> [!tip] Medidas mais comuns
> - Euclidianas 
> - minkowski
> - Cosseno
> - Pearson


## Etapas de Agrupamento
3. Etapa de agrupamento: utilização de alguma estratégia/técnica de agrupamento

### Agrupamento Hierárquico
- Construção de Árvores de clusters 
- Métodos Aglomerativos:
    - Cada objeto x é um cluster. Agrupamos, em seguida, 2 objetos próximos. Paramos usando algum critério (limiar de parada, i.e 20 clusters) ou até um grande cluster.
    - Ligação Individual: menor distância entre qualquer objeto de um grupo até qualquer outro objeto de outro. Geram grandes cadeias e clusters alongados. 
    - Ligação Completa: maior distância de todos os objetos em um grupo para os demais em outro. Geram pequenas cadeias.
    - Ligação Média.

### K-means (K-médias)
Baseado em centroide. Podemos medir a qualidade por variância intracluster.
- Passo 1: Os primeiros k centros dos aglomerados são escolhidos aleatoriamente.
- Passo 2: Cada objeto é atribuído ao grupo associado com o centro mais próximo.
- Passo 3: Um novo centro para cada grupo é calculado pela média dos valores de todos os objetos – centroide).
- Passo 4: O Passo 2 (com os novos centros) e Passo 3 são então repetidos até que não haja mudança nos centros.

#### Método do Cotovelo

TODO

### Mean Shift

## Etapa de Validação

4. Etapa de validação: Etapa em que determinamos se os clusters são significativos, ou seja, se a solução obtida é representativa para o conjunto de dados analisado.

### Análise de Silhueta
Silhueta média (de todos os pontos): fornece uma medida da qualidade para o agrupamento.

Quanto maior for a silhueta média (=1), melhor é o agrupamento. Valores negativos ou próximos de 0 indicam que os clusters podem não estar bem separados.


$$
s(i) = \frac{b(i) - a(i)}{max{a(i), b(i)}}
$$


## Etapa de Interpretação 
Examinar cada cluster construido. 
