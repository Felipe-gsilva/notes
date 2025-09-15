Exercicio (Sala):
Encontrar os conjuntos Primeiro e Seguinte

a) S -> AB
   A -> c|$\epsilon$
   B -> cbB|ca 

b) S -> XYZ
    X -> aXb|$\epsilon$
    Y -> cYZcX|d
    Z -> eZYe|f

Exercicios (Casa):
Construir os diagramas sintaticos e o ASDR:
- entrada->expressao _eof_
- expressao->termo expressao_restante
- termo -> _id_ | expressao_entre_parenteses
- expressao_entre_parenteses -> ( expressao )
- expressao_restante -> expressao | $\epsilon$

---

# Analise Sintatica Preditiva Não Recursiva

Algoritmo: Construção da tabela de análise sintática Preditiva

Entrada: gramática G 
Saída: tabela sintática M 
Método:

1. Para cada produção $A  \rightarrow \alpha$, faça os passos 2 e 3:
2. Para cada terminal $a$ em Primeiro($\alpha$), adicione a produção $A  \rightarrow \alpha$ à entrada $M[A, a]$.
3. Se $\epsilon$ estiver em Primeiro($\alpha$), adicionar $A \rightarrow \alpha$ em $M[A, b]$ para cada terminal b em Seguinte(A). Se $\epislon$ estiver em Primeiro($\alpha$) e $b$ for (\$), adicione $A \rightarrow \alpha$ em $M[A, \$]$.


Exercicio: Construir a tabela de analise sintatica preditiva para a seguinte gramática

E-> TE'
E'-> +TE' | $\epsilon$
T-> FT'
T'-> *FT' | $\epsilon$
F-> (E) | id


| não terminal | id | + | * | ( | ) | $ |
|---------------|----|---|---|---|---|---|
| E             | E-> TE' |   |   | E-> TE' |   |   |
| E'            | | E'-> +TE' |   | | E'-> ε |  E'-> ε |
| T             | T-> FT' |   |   | T-> FT' |   |   |
| T'            | | T'-> ε | T'-> *FT' | | T'-> ε | T'-> ε |
| F             | F-> id |   |   | F-> (E) |   |   |


posições em branco na tabela representam erros de análise sintática.
