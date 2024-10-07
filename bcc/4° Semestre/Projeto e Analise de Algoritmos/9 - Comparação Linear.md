O modelo de árvore de decisão:
- uma árvore binária cheia que representa comparações entre elementos para obter informações de ordem para uma sequência de entrada. Isto é, dados 2 elementos $a_{i}$ e $a_{j}$ executamos um dos testes $a_i< a_j, a_i \leq a_j, a_i = a_j, a_i > a_{j} \ ou \  a_{i} \geq a$

## props
- cada nó interno é tido como um intervalo do vetor $i:j$.
- cada folha é uma permutação entre os elementos do vetor.

# Ordenação por contagem
Uma ordenação por contagem supõe que cada um dos n elementos de entrada é um inteiro na faixa 1 a k, para algum inteiro k. Quando k = $O(n)$ a ordenação é executada no tempo n.

A ordenação por contagem determina, para cada elemento de entrada x, o número de elementos menores que x e usa essa info para inserir o elemento x diretamente eu sua posição no arranjo de saída.

- não aceita números negativos
- o vetor C conta a quantidade de valores em A iguais a $i$

![[Pasted image 20241007105202.png]]
