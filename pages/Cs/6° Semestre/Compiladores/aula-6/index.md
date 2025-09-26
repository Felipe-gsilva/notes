# Algoritmo de Análise Sintática Descendente Não Recursivo (ADNR)
Essa análise sintática usa a tabela preditiva, vista anteriormente.

*Entrada*: $w$ e $M$ (tabela sintática preditiva)

*inicio*
│   $ip$ aponta para o primerio simbolo de $w$
│   empilha $\$$
│   empilha o simbolo inicial da gramática
│   *repetir*
│   │   seja $X$ o simbolo no topo da pilha
│   │   seja $a$ o simbolo apontado por $ip$
│   │   se $X$ é um terminal então
│   │   │   *se* $X$ = $a$ *então*
│   │   │   │   desempilha $X$
│   │   │   │   avança $ip$
│   │   │   *senao*
│   │   │   │   erro de análise sintática
│   │   *senao se* $X$ é *não-terminal* e $M[X,a]$ = $X \rightarrow Y_1 Y_2 \dots Y_k$ *então*
│   │   │   desempilha $X$
│   │   │   empilha $Y_k, Y_{k-1}, \dots, Y_1$ (se $k$ = 0, nada é empilhado)
│   │   *senao*
│   │       erro de análise sintática
│   *até que* $X = \$ $
*fim*

Exercicio (sala): feito no caderno

Exercicio (casa):  repita o exercicio feito no caderno, utilizando a cadeia de entrada:

a) id + id * idid
b) id * id ** id + id
