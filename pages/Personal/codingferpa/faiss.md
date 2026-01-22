
# Faiss -  High-Performance Vector Similarity Search and GPU K-Selection

A biblioteca faiss é uma biblioteca feita pela Meta de alta performance para pesquisa em vetores por similaridade, especialmente eficiente para vetores densos.

Abaixo, vou elencar os principais tópicos de funcionalidade e aplicações possiveis (na apresentação esta ordem pode ser distinta):

## Fundamentos 

Dado um conjunto de vetores $x_i$ em uma dimensão qualquer $d$, a biblioteca constrói uma estrutura de dados chamada de índice em memória RAM. Após mapear todos os vetores nesse espaço de $d$ dimensões, podemos comparar agora um vetor qualquer (de mesma dimensão) com a base de dados em memória INTEIRA, sendo  o objetivo final encontrar o vetor que:
- maximiza o produto escalar entre ambos
- minimiza a distância euclidiana ($L^2$) entre ambos
- maximiza a similaridade de cosseno (via normalização $L^2$)


> Espera-se que os vetores dados sejam identificados cada um por um valor inteiro distinto.

Para isso, o faiss utiliza-se do conceito HNSW - Hierarchical Navigable Small World


## Otimizações 

### Clustering
o faiss calcula o centroide de um vetor, utilizando-se o algoritmo lloyd's k-means. O usuario insere um valor que diz quantos centroides quer usar, normalmente $\sqrt{l}$ onde $l$ é o número de vetores no espaço, ai, o cálculo de média entre os vetores naquela célula é o que define o melhor centróide, gerando o quantizador q1 e as listas das células num arquivo de indice invertido.

Isso permite comparar o vetor de consulta com uma fração muito menor do dataset. Ai quando o centróide é promissor, o cálculo passa a ser entre os vetores completos dentro dos $\omega$ centroides mais proximos.

Temos que:
$q_1(y) = argmin_{c\inC_1}\lVert y - c \rVert^2$

assim, temos a(s) lista(s) de maior similaridade.


Tabelas de Busca Pré-computadas
Algoritmo WarpSelect (k-selection)


## Funcionalidades diretas

- Busca exata: brute force mesmo onde se compara com boa parte do índice para o maior retorno.
- Busca por range: retorna todos os k vizinhos dentro de um raio de distância especifico
- Busca em lote:  exatamente o que se espera, vale pras 2 acima


## Aplicações
