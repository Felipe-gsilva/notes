# Condições de Paralelismo

Nem tudo pode ser paralelizado, mas mesmo o que pode tem suas restrições.

São 3:
1. Dependência de recursos (recursos fisicos de fato).
2. Dependência de controle (controle de fluxo, com condicoes - x < 50 por exemplo)
3. Dependência de dados (ou condições de Bernstein).
    - fluxo: ocorre quando os resultados (saida) de um grupo de instrucoes S1 sao entrada de S2.
    - anti-dependencia: quando a saida de S2 é entrada de um grupo S1 que o anteceda sequencialmente.
    i.e: A = 2; X = A + 1; A = 5
    - saida: 2 grupos tem saida em comum. 
    i.e: A = 2;  A = 5

## Bernstein
Processo ($P_i$): fragmento de um programa.
Entrada: ($I_i$): entradas necessarias para executar $P_i$
Saida: ($O_i$): saidas produzidas ao executar $P_i$

2 processos podem executar em paralelo ($P_i//P_k$; $i < k$) se:
    - $I_i \cap O_k = \emptyset$ => anti-dependencia
    - $I_k \cap O_i = \emptyset$ => fluxo
    - $O_k \cap O_i = \emptyset$ => saida


Construimos um grafo dirigido com cada programa sendo um vertice


Grao: conjunto de instrucoes que precisa ser executada de forma sequencial. 
Pode ser fino, medio e grosso. 

Mais Fino Possivel: ILP (instruction-level paralelism) -> demanda muito controle e comunicação, normalmente controlado pelo compilador.

Grão médio: envolvem procedimentos, funções, rotinas, tarefas, etapas de um trabalho ou parte pouco complexas de um programa. 

Grão Grosso: envolvem programas inteiros ou partes complexas do programa. Há um pequeno grau de paralelismo. Há pouca necessidade de controle, é usdo em sistema de mensageria, como clusters.


