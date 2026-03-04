# Fundamentos de Aprendizado de Máquina 

- Introdução 
- Aprendizado Supervisionado 
- Aprendizado Não Supervisionado 
- Aprendizado por Reforço 
- Conceitos e definições 
- Modelo de Regressão linear 
- Classificador Linear

## Glossario 

- Regressão = números contínuos como saída 
- Classificação = classes discretas como saída 
- Classificação binária e multclasse são tratados de maneira diferente.
- Univariado = uma única saída 
- Multivariado = mais de uma saída 

## Introdução 

Machine Learning está para Inteligência Artificial, assim como deep learning está para machine learning. Essas áreas são subáreas da subsequente área mais ampla e compartilham entre si conceitos similares. Ainda assim, têm como base as redes neurais. Elas permitem que outras subáreas se desenvolvam, como:

## Aprendizado Supervisionado

Define-se como o modelo com capacidade aprender mapeamento de uma entrada para uma saida (em fase de testes, já conhecida).

Dado pela função $y = f(x)$, dado um conjunto de equações finitas possíveis, busca-se encontrar os valores dos parâmetros que melhor se ajustem às saidas esperadas.

Para isso, podemos utilizar alguns algoritmos: 

- Regressão Logistica
- SVM - support machine vector
- Árvore de decisão
- Random Forest 
- kNN - k Nearest Neighbor
- Redes Neurais Artificiais
- Naive Bayes

para os seguintes problemas:

- Regressão univariada: uma saída real (Fully Connected Network).
- Regressão em grafos: multivariada, mais de uma saida. (Graph Neural Network).
- Classificação (binária): 2 classes discretas, baseado em transformers.
- Classificação (multiclasse): n classes discretas (Recurrent Neural Network e Convolutional Neural Network).
- Segmentação de Imagens, Estimativa de profundidade, pose, tradução automática entre outros...

## Aprendizado Não-Supervisionado




## Aprendizado por Reforço


### Loss 

$$
L [\phi, f\[x, \phi\], (x_i,y_i)_{i=1}^l]
$$
