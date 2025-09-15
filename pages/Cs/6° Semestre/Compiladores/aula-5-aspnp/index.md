# Analise Sintática Preditiva Não Recursiva

Algoritmo: Construção da tabela de análise sintática Preditiva

Entrada: gramática G 
Saída: tabela sintática M 
Método:

1. Para cada produção $A  \rightarrow \alpha$, faça os passos 2 e 3:
2. Para cada terminal $a$ em Primeiro($\alpha$), adicione a produção $A  \rightarrow \alpha$ à entrada $M[A, a]$.
3. Se $\epsilon$ estiver em Primeiro($\alpha$), adicionar $A \rightarrow \alpha$ em $M[A, b]$ para cada terminal b em Seguinte(A). Se $\epsilon$ estiver em Primeiro($\alpha$) e $b$ for (\$), adicione $A \rightarrow \alpha$ em $M[A, \$]$.
