# Bison (parser generator)

- Preambulo: declaração dos tokens, artefatos, ordem de precedência e etc.
```c
%{
    #include <stdio.h>


%}
```
- Gramática (LLR):
 - funções: seção de funções auxiliares

## Compilação

O código Bison deve ser transformado em código C, via comando:

```sh
bison -d -v parser.y
```

Logo em seguida deve ser compilado via g++ 

```sh
gcc parser.tab.c -lfl 
```

# Integração com flex

- parser.tab.c:
- parser.tab.h: podemos incluir no flex
- parser.output: descrição da gramática gerada

```c 
%{
#include "parser.tab.h"
%}

```

o arquivo flex não terá mais uma função auxiliar main, ou seja, o bison terá que tê-la.

A maneira mais direta de trasnferir dados entre as 2 ferramentas é utilizando yylval que funciona como uma variável global. Os valores devem ser escritos no flex e apenas lidos no Bison para armazenar o estado do parser é necessário programar as próprias estruturas.

---
# Aula normal

S -> a | \[L\]
L -> L; S | S

feito no caderno

# Construção de uma LR(1)

Faça a construção do conjunto de itens baseado na seguinte gramática:

S -> CC 
C -> cC | d 

.
.
.

Aumentamos a gramatica:

S' -> S
S -> CC 
C -> cC
C -> d

Precisamos descobrir os conjuntos PRIMEIRO e SEGUINTE da gramatica:

first(S) = {c, d}
first(C) = {c, d}

## Cálculo dos Conjuntos de Itens LR(1)

$I_0$ = {
    S' -> .S, \$
    S -> .CC, \$
    C -> .cC, c/d 
    C -> .d, c/d
}

$I_1$ = {
    S' -> S., $
}

$I_2$ = {
    S -> C.C, \$
    C -> .cC, \$
    C -> .d, \$
}

$I_3$ = {
    C -> c.C, c/d
    C -> .cC, c/d
    C -> .d, c/d
}

$I_4$ = {
    C -> d., c/d
}

$I_5$ = {
    S -> CC., \$
}

$I_6$ = {
    C -> c.C, \$
    C -> .cC, \$, 
    C -> .d, \$
}

$I_7$ = {
    C -> d., \$
}

$I_8$ = {
    C -> cC., c/d
}

$I_9$ = {
    C -> cC., \$
}

## Construção tabela sintática
quase igual, so precisa olhar ao inves do proximo(A), olhar para o lado direito 

tarefa: começar a construir a tabela 
