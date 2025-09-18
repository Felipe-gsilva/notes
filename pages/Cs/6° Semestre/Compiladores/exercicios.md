AULA 1

---
AULA 2
Identifique os tokens:
	int a,b,c;
	char cadeia;
	leia(a);
	b = 3;
	c = 2;
	c = c + a + b;
	escreva(c);
	Cadeia = 'S';
	escreva(S);	

---
AULA 3

---
AULA 4
Exercício(casa): usando derivação, obtenha 10 cadeias da linguagem abaixo
$G = ({E, E', T, T'}, {+,-,*,/,num}, P, E)$
$P:  E -> TE'$
	$E' \rightarrow +TE' | - TE' | \epsilon$
    $T \rightarrow FT'$
    $T' \rightarrow *FT' | /FT' | \epsilon$
    $F \rightarrow (E) | num$

Exercícios: Calcule o conjunto First e Seguinte
a) 
  $E \rightarrow TE'$
  $E' \rightarrow +TE' \ | \ - TE' \ | \ \epsilon$
  $T \rightarrow FT'$
  $T' \rightarrow \ *FT' \ | \ FT' \ | \ \epsilon$
  $F \rightarrow (E) \ | \ num$

b)  $S\rightarrow aAeS \ | \ Bd \ | \ d$
	$A\rightarrow aA \ | \ \epsilon$
	$B\rightarrow bB \ | \ c$

---
AULA 5

Exercício (Sala):
Encontrar os conjuntos Primeiro e Seguinte

a) S -> AB
   A -> c|$\epsilon$
   B -> cbB|ca 

b) S -> XYZ
    X -> aXb|$\epsilon$
    Y -> cYZcX|d
    Z -> eZYe|f

Exercícios (Casa):
Construir os diagramas sintaticos e o ASDR:
- entrada->expressao _eof_
- expressao->termo expressao_restante
- termo -> _id_ | expressao_entre_parenteses
- expressao_entre_parenteses -> ( expressao )
- expressao_restante -> expressao | $\epsilon$


Exercicio: Construir a tabela de analise sintática preditiva para a seguinte gramática

E-> TE'
E'-> +TE' | $\epsilon$
T-> FT'
T'-> *FT' | $\epsilon$
F-> (E) | id


| não terminal | id      | +         | *         | (       | )      | $      |
| ------------ | ------- | --------- | --------- | ------- | ------ | ------ |
| E            | E-> TE' |           |           | E-> TE' |        |        |
| E'           |         | E'-> +TE' |           |         | E'-> ε | E'-> ε |
| T            | T-> FT' |           |           | T-> FT' |        |        |
| T'           |         | T'-> ε    | T'-> *FT' |         | T'-> ε | T'-> ε |
| F            | F-> id  |           |           | F-> (E) |        |        |

posições em branco na tabela representam erros de análise sintática.