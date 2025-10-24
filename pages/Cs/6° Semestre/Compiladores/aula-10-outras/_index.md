Exercicio:

S -> id | V = E
V -> id 
E -> V | n

Gramatica aumentada

1. S' -> S 
2. S -> id
3. S -> V = E
4. V -> id
5. E -> V
6. E -> n

a) Construa a tabela de análise preditiva LR(1) para a gramática acima.

first sets:
first (S) = {id}
first (V) = {id}
first (E) = {id, n}

$I_0$ = {
    S' -> .S, \$
    S -> .V = E, \$ 
    S -> .id, \$
    V -> .id, =
}
$I_1$ = {
    S' -> S., \$
}

$I_2$ = {
    S -> id., \$
    V -> id., =
}

$I_3$ = {
    S -> V. = E, \$
}
$I_4$ = {
    S -> V = .E, \$
    E -> .V, \$
    E -> .n, \$
    V -> .id, \$
}
$I_5$ = {
    E -> n., \$
}
$I_6$ = {
    E -> V., \$
}
$I_7$ = {
    V -> id., \$
}
$I_8$ = {
    S -> V = E., \$
}


--- 
Construção da tabela de análise preditiva LR(1):

| Estado | id      | =       | n       | $       | S       | V       | E       |
|--------|---------|---------|---------|---------|---------|---------|---------|
| 0      | s2 | | | | 1 | 3| |
| 1      | | | | acc | | | |
| 2      |  | r4 | | r2 | | | |
| 3      | | s4| | | | | |
| 4      | s7 |  | s5 | | | 6 | 8 |
| 5      | | |  | r6 | | | |
| 6      | | |  | r5 | | | |
| 7      |  | | | r4| | | |
| 8      | | | | r3 | | | |


---


