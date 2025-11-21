# Tecnicas de Otimização de código
Precisa-se das medidas de desempenho em mão.

Pontos críticas de otimização:
- Linguagem (ou estruturas utilizadas): estruturas estaticas, simples e homogeneas sao usualmente mais rapidas e quanto menores melhores em comparacao a estruturas hetereogenas, dinamicas e de ponteiros (nem sempre eh possivel)
- Funções: deve-se evitar o uso de funções curtas, preferindo-se usar definições de macros (function inlining).
- Blocos de repetição: maior fonte para otimizações: 
1) Desdobramento de código
2) Remoção de testes desnecessários
3) Inversão de aninhamentos
4) Fissão ou fusão de laços


## Desdobramento de código
```c
// inicialmente
for (i=0; i<N; i++)
    A[i] = A[i] + B[i] * C;

// se torna
for (i=0; i<N; i=i+4)
{ A[i] = A[i] + B[i] * C;
    A[i+1] = A[i+1] + B[i+1] * C;
    A[i+2] = A[i+2] + B[i+2] * C;
    A[i+3] = A[i+3] + B[i+3] * C;
}

// Desdobramento de ciclos
ii = N % 4;

for (i=0; i<ii; i++)
    A[i] = A[i] + B[i] * C;

for (i=ii; i<N; i=i+4)
{ A[i] = A[i] + B[i] * C;
    A[i+1] = A[i+1] + B[i+1] * C;
    A[i+2] = A[i+2] + B[i+2] * C;
    A[i+3] = A[i+3] + B[i+3] * C;
}
```
## Remoção de testes desnecessários
Muitas vezes fazemos testes que, a menos por precisão, poderiam ser evitados

Podemos tirar testes com invariantes (constantes) completamente do código.

Testes que nao podem ser removidos com desdobramento podem ainda ser paralelizados se o hardware permitir loop unrolling ou processamento vetorial.

### Inversão de aninhamentos
Ciclos aninhados usualmente representam acesso a matrizes. A ordem de acesso a elementos de matrizes pode ser otimizada para melhorar o uso do cache.

```c
// inicialmente
for (i=0; i<N; i++)
    for (j=0; j<N; j++)
        A[i][j] = A[i][j] + B[i][j] * C;

// se torna
for (j=0; j<N; j++)
    for (i=0; i<N; i++)
        A[i][j] = A[i][j] + B[i][j] * C;
```

### Fissão ou fusão de laços

Fusão de laços é possível quando dois laços consecutivos operam sobre os mesmos indexadores de controle.

Fissão de laços é possível quando um laço realiza operações independentes que podem ser separadas em dois ou mais laços.

```c 
// inicialmente
for (i=0; i<N; i++) {
    D[i] = D[i] + E[i] * F;
}

for (i=0; i<N; i++) {
    A[i] = A[i] + B[i] * C;
}

// fusão de laços
for (i=0; i<N; i++) {
    A[i] = A[i] + B[i] * C;
    D[i] = D[i] + E[i] * F;
}
// fissão de laços
for (i=0; i<N; i++) {
    A[i] = A[i] + B[i] * C;
}
for (i=0; i<N; i++) {
    D[i] = D[i] + E[i] * F;
}
```

## Trabalho do compilador 

1) Propagação de código: quando uma expressão ou atribuição é repetida, o compilador pode substituir a expressão pelo seu valor já calculado anteriormente.
2) Renomeação de variáveis: quando duas variáveis não interferem entre si, o compilador pode renomear uma delas para evitar conflitos e melhorar a eficiência.
3) Desdobramento de constantes: quando uma variavel é calculada e tem valor constante, o compilador pode substituir a variavel pelo valor constante diretamente no código.
4) Redução de força: alterar operações custosas por mais simples. Exemplo: substituir multiplicações por somas repetidas.

# Técnicas de Avaliação de Desempenho
