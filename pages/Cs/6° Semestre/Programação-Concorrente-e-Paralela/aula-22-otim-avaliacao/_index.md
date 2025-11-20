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


