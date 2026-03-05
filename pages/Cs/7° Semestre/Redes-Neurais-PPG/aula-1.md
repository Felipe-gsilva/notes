# Fundamentos de Aprendizado de Máquina 

- Introdução 
- Aprendizado Supervisionado 
- Aprendizado Não Supervisionado 
- Aprendizado por Reforço 
- Conceitos e definições 
- Modelo de Regressão linear 
- Classificador Linear

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

Não precisa de rótulos nos dados e tende a se relacionar com problemas de agrupamento ou geração de dados novos. Definindo, um modelo de aprendizado Não-Supervisionado precisa aprender padrões de dados sem rótulos, com a saída diretamente associada a entrada.

Deste modo, problemas como:
- agrupamento 
- detecção de outliers num conjunto de dados
- aumento de dados 
- redução de dimensionalidade 
- preenchimento de dados 

e utiliza-se de algoritmos como: 
- K-means 
- Hierarchical Clustering 
- Autoencoders 
- PCA - Principal Component Analysis - 
- t-SNE (t-distributed Stochastic Neighbor Embedding)  - é um algoritmo de aprendizado de máquina não linear usado para visualização de dados complexos de alta dimensionalidade em mapas 2D e 3D. Ele agrupa pontos similares sendo ideal para identificar clusters, padrão e estruturas locais.
- auto-supervisionados

## Aprendizado por Reforço

Caraterizado por ter um finitos conjuntos de estados, ações e recompensas atribuidas para as reações corretas esperadas. No entanto, esse tipo de treinamento torna-se muito difícil devido a alguns embróglios:
- estocasticidade: mesmas ações e reações podem levar a diferentes respostas.
- atribuição temporal de crédito: identificar a origem de uma boa ação é difícil, visto que uma ação recente pode não ser a responsável pelo sucesso atual, mas uma antiga (ou vice-versa).
- dilema de exploração ou explotação: em certos momentos, arriscar uma nova escolha pode ser mais proveitoso (exploração). No entanto, uma ação já conhecida pode ser exploitada se a recompensa é boa o suficiente, o que não é ótimo.


## Conceitos e definições 

- problema de:
    - Regressão = números contínuos como saída 
    - Classificação = classes discretas como saída 
    - Classificação binária e multclasse são tratados de maneira diferente.
        - Univariado = uma única saída 
        - Multivariado = mais de uma saída 

- inferência: modelo roda os processos apenas para computar a saída a partir de qualquer entrada válida (sem treino, validação ou teste).
- parâmetros (de um modelo): são as variáveis internas e configuráveis que um modelo aprende durante o treinamento.
- treinamento: encontrar os parâmetros que prevejam as saidas de forma eficaz a partir dos dados do treino.

- overfitting: um modelo perde a capacidade de generalizar o aprendizado, apenas decora as caracteristicas dos dados treino. Assim, a acurácia no treino é alta e na validação ou teste não.
- underfitting: processo contrário, onde o modelo generaliza tanto que não se adapta aos dados, ou seja, o resultados não tem ligação com a entrada. Baixo desempenho em treino ou teste.

- indução: capacidade do modelo em aprender padrões a partir de exemplos específicos.
- viés indutivo: suposições que o modelo faz para poder induzir (nem sempre corretas).

- função de mapeamento: $y = f[x, \phi]: f[x, \phi] \approx y$
onde $x$ são as entradas, $y$ são as saidas, $]phi$ são os parâmetros.

- função de Loss (custo) é dada por $ L [\phi, f\[x, \phi\], (x_i,y_i)_{i=1}^l] $

- fases de:
    - treino: fase onde o modelo altera os parametros para aprender.
    - validação: ajustar hiperparâmetros, evitando overfitting.
    - teste: avaliar o desempenho real do modelo em inferência para novos dados.

- cross validation é uma técnica robusta de machine learning usada para avaliar o desempenho de um modelo ao dividir o dataset em partes menores, por exemplo, usando k-folds (os dados de treino são dividos em k pastas distintas e k treinamentos, portanto, evitando overfitting e um especifico para treino).

- métricas de regressão: 
    - MAE: mean absolute error 
    - MSE: mean square error 
    - RMSE: root mean squere error

- matriz de confusão: permite calcular acurácia, precisão, recall, F1 score, AUC entre outros.
