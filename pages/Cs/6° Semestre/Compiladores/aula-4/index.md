# Continuação analise sintatica descendente

- sem retrocesso
- chamado analisador sintatico preditivo.
- adequado para gramaticas LL(1) -> left-to right -> lelf (derivações) -> (k-lookahead = 1)

2 tipos de AS (analisadores sintaticos) preditivos: 
- recursivo: associa uma funcao para cada simbolo nao terminal da gramatica.
- nao recursivo: usa uma tabela que indica quais regras de producao devem ser usadas.

Exercicio(casa): usando derivacao, obtenha 10 cadeias da linguagem abaixo
G = ({E, E', T, T'}, {+,-,*,/,num}, P, E)
P:  E -> TE'
    E' -> +TE' | - TE' | $\epsilon$
    T -> FT'
    T' -> *FT' | /FT' | $\epsilon$
    F -> (E) | num


## Construir um analisador sintático descendente recursivo para G

```py
# nao funciona
token: str = None

def ASDR():
    try:
        token = solicita_token(analex)
        e(token)
    except Excepetion as e:
        print(e)

def e(token):
    t(token)
    e_linha(token)

def t(token):
    f(token)
    t_linha(token)

def e_linha(token):
    if token.value == "+" or token.value == "-":
        token = solicita_token(analex)
        t(token)
        e_linha(token)

def f(token):
    if token.value == "(":
        token.value = solicita_token(analex)
        e()
        if token.value == ")":
            return
        throw new Error("Nao fechou parenteses")

    if token.type == num:
        return

    throw new Error("Nem parenteses nem numero")

def t_linha(token):
    if token.value == "*" or token.value == "/":
        f()
        t_linha()
```


## Quando usar um ASDR
-> poucas regras gramaticais 
-> linguagens de programação possui recursividade
-> ATENÇÃO: a GLC não pode ser recursiva à esquerda

Exercício: construir os diagramas (caderno)

# Eliminação de recursividade à esquerda
$A -> A\alpha |\beta$ pode ser substituído por:
$A -> \beta A'$
$A' -> \alpha A' |\epsilon$

outro exemplo:
E -> E + T | T

vira: E -> TE'
      E' -> +TE' | $\epsilon$


# Analise Sintatica Produtiva
![[Pasted image 20250829102631.png]]

# First and Follow
necessários para construir um analisador sintático preditivo, podendo prever a regra de produção correta.

## First(Primeiro)
1. Se X for terminal, Primeiro (X) = {x}
2. Se X -> $\epsilon$ for uma produção, adicione $\epsilon$ a Primeiro(X)
3. Se X for não-terminal e $X \rightarrow Y_1, Y_2,\ \dots,\ Y_n$ uma produção, colocar a em primeiro (X) se para algum $i$, a estiver em Primeiro($Y_i$), e $\epsilon$ estiver em todos: Primeiro($Y_1$) $\dots$ Primeiro($Y_{i-1}$), isto é, se $$Y_1\dots Y_{i-1}\xRightarrow{y} \ \epsilon$$
Se $\epsilon$ estiver em Primeiro($Y_j$), $j = 1,\ 2 \ \dots \ n$, então adicione $\epsilon$ a Primeiro(X).

## Follow(seguinte)
1. colocar $ em Seguinte(S), S símbolo de partida.
2. Se existir uma produção A->$\alpha B \beta$, então tudo em Primeiro($\beta$) está em Seguinte($\beta$) exceto $\epsilon$
3. Se existir uma produção A->$\alpha B\beta$ onde Primeiro($\beta$) contém $\epsilon$, então tudo em Seguinte de A está em Seguinte($B$).

Exercícios: Calcule o conjunto Primeiro e Seguinte
a) 
  E -> TE'
  E' -> +TE' | - TE' | $\epsilon$
  T -> FT'
  T' -> \*FT' | /FT' | $\epsilon$
  F -> (E) | num

b)  S->aAeS|Bd|d
	A->aA|$\epsilon$
	B->bB|c