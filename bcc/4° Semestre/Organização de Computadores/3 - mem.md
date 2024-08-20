- somente LOAD/STORE devem referenciar a memória.
- necessários mts registradores, trabalhando em uma pipeline unica ou dividida em threads fisicas e/ou logicas, onde cada registrador manipulado pode ser parte do processo.

#Memoria #cache #ram
# Memória

Dividida em células (ou locais) os quais são referenciados por um endereço único e indicado para cada célula.
- os bytes em uma palavra podem ser organizados 
	- big endian -> da esquerda pra direita 
	- little endian->da esquerda pra direita 

![[Pasted image 20240814174741.png]]
> devido a possibilidade de falhas, faz-se necessária a detecção de erros.

### Código de Hamming -> na memória
Para detectar $d$ erros de um único *bit*, é preciso manter um código de distância $d+1$ e para corrigi-lo, precisa-se de $2d+1$. Ou seja, se der erro em 1 bit, precisaríamos de um total de 5 para resolver o erro. São escolhidos então, $2d+1$ bits de paridade para averiguar 

;; TODO

## Cache
Memória mais veloz, portanto, prefere-se a manter as palavras mais usadas no processamento dentro delas.