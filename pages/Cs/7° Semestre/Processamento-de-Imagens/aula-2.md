# Introdução


Para nossa visão, perceber uma imagem (não digital), precisamos de:
- fonte de luz
- luz: onda eletromagnética e estimula nossos olhos, que traduzem essas ondas para:
    - cor: definida pelo comprimento de onda


Para, portanto, usar imagens, temos que ter um pipeline explicito de algumas etapas, que chamamos de sistema visual: 

- aquisição
- Pré-processamento 
- segmentação 
- representação e descrição 
- reconhecimento e interpretação

a qual nos gera uma imagem. Essa imagem, no entanto, é uma imagem analógica e infinita. Mas o que é uma imagem?

## Imagem

Uma imagem pode ser definida como uma função bi-dimensional f(x,y), onde x e y são coordenadas espaciais e a amplitude de f para cada tupla (x,y) é chamado de intensidade ou nível de cinza da imagem, ou seja, pode ser tratada como uma distribuição de valores numéricos quaisquer, desde que tenha algum sentido para futura reprodutibilidade. 

Quando esses valores, f(x,y), x e y são finitos e discretos, chamamos a imagem de uma imagem digital, composta por elementos, portanto. Um pixel é o termo mais usado para cada elemento de uma imagem.

Como previamente dito, temos, majoritariamente, imagens analógica e precisamos digitalizá-las, utilizando-nos de: (i) amostragem: processo de selecionar parte representativa da imagem analógica e (ii) quantização: mapear os valores infinitos de cores de cada elemento da imagem para um valor discreto, valores os quais podemos escolher dentre variados sistemas.

## Sistemas de Cores 
Verificar [aula de CG]("../../6° Semestre/Computação-Gráfica/aula-1-intro/intro+cores.md").

## Sinais 
Um sinal é uma manifestação de um fenômeno expresso de forma quantitativa. Pode ser representado por uma função. Pode tambem ser analógico (variações contínuas no tempo) ou digital (valores discretos).

Resolução espacial: quanto menor o intervalo ($\Delta x$), maior a densidade de pixels e maior a resolução espacial.

Luminância: valor associado a cada pixel (tom de cor).

Profundidade: quantidade de bits usado na quantização.

Imagem multi banda: mais de um canal.
