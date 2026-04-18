# Support Vector Machines (SVM)
Solução: empregar o conceito de margem máxima para encontrar o melhor hiperplano.
Intuição: quanto mais longe uma instância de dados estiver do limite de decisão, maior será o grau de confiabilidade.

## Margem Máxima 
- Distância da instância $x^{(i)}$ até o hiperplano separador: $r =\frac{|w^tx^{(i)} + b|}{||w||}$

- As instâncias mais proximas do separador são chamadas de vetores de suporte.

- Margem $\rho$ do separador: é a distância entre os 2 hiperplanos de suporte, tentando maximizar $\rho$.

## Modelagem Matemática

- Entrada: $(x^{(i)}, y^{(i)}) \dots (x^{(n)}, y^{(n)})$, com $x^{(i)} \in X \subset R^m$ e $y^{(i)} \in \{-1, 1\}$

Queremos construir um classificador linear, podemos usar uma ativação do tipo sinal (tal qual o perceptron).

Em um espaço m-dimensional, o hiperplano é dado por $f(x) = 0 \implies w^tx +b = 0$, sendo $w$ o vetor normal do hiperplano. Dado que $f(x)$ é invariante à escala $\forall \lambda \neq 0$, desta forma, travaremos a escala em $\lambda = 1$, travando o tamanho do vetor normal.


A distância entre um ponto $s$ e o hiperplano é o comprimento do segmento perpendicular à linha até s.

$s - z = \lVert s - z \rVert \frac{w}{\lVert w \rVert}$

A margem é dada ao definir o hiperplano separador de forma que ele seja equidistante aos pontos mais próximos das classes.

Logo, a ideia é maximizar a margem sujeito à: $ y^{(i)}(w^tx^{(i)} + b) \geq 1$

Para calcular isso, podemos usar $w^tx + b = 1$ e $w^tx + b = -1$.

Logo, a margem $\rho = \frac{1}{\lVert w \rVert}$, e o que queremos: 
$\max_{w, b}{\frac{1}{\lVert w \rVert}}$

ou, ainda $min_{w, b}\frac{1}{2}\lVert w \rVert^2$

sujeito à $y^{(i)}(w^tx^{(i)} + b) - 1 >= 0, \forall i$.

Esse problema, chamado de Problema de Programação Quadrática, o qual recai na classe de problemas de otimização convexa.


## Modelagem Suave 

TODO

## SVM Não Linear

Temos que aumentar o espaço da entrada e projetar o hiperplano de dimensão maior na dimensão menor, via embedding.

### Truque do kernel

TODO
