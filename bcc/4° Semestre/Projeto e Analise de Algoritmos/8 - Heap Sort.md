### conteudo pra Eng. software bom
Sort -> saiba o merge sort.
Tabela Hash -> esteja preparado pra explicar uma tabela hash e saiba como implementá-la.
Usar API, uma lang, conhecimento de design e POO, dijkstra, A*
ED-> dinâmicas, tabela hash, dicionário, heap e grafos.
Matemática discreta 
AVL, DFS, BFS, Dijkstra e A* 

---
# heap
- árvore binária quase-completa
- vetorizada.
- filho a esquerda de i (2i) 
- filho a direita de i(2i +1)
- pai de i = i/2 
- A[0] = raiz da árvore
## heap máximo e minimo
_máximo_ $A[PAI(i)] \geq A[i]$  maior elemento está na raiz, menor na ultima folha a direita 16 -> 1
_minimo_ $A[PAI(i)] \leq A[i]$ o contrário
# Heap Sort

Heap Sort -> ordenação in-place: um numero constante de elementos do vetor é armazenado 
- construido com heap

Complexidade = $O(\lg{n})$

_MAX_HEAPIFY_. 
> Se algum filho for maior que o pai atual, trocaremos ele com o maior filho e faremos a mesma verificação com o filho escolhido.

``` c
void max_heap(heap *A, int i) {
	int l = 2i;
	int r = 2i+1;
	int maior = 0;

	if (l <= A->size && A[l] > A[r]) {
		maior = l; 
	}
	else
		maior = i;
	if (r <= A->size && A[r] > A[maior])
		maior = r;
	if (maior != i){
		swap(A[i], A[maior]);
		max_heapify(A, maior);
	}
}
```

_BUILD_MAX_HEAPIFY_
o sub-vetor de $A(\lfloor \frac{n}{2}\rfloor +1 : n)$ não precisa ser alterado. 
Essa função começa de $i = \frac{n}{2}$ a cada iteração executando _MAX_HEAPIFY_ 
``` c
void max_heapify(heap *A) {
	A->size = A->length;
	for(int i = n/2; i > 0; i--)
		max_heap(A, i);
}
```
invariante de laço: No começo de cada iteração do laço for das linhas 2-3, cada nó i+1, ..., n é a raiz de um heap máximo.

_HEAPSORT_ 
``` c
void HEAP_SORT(heap *A) {
	BUILD_MAX_HEAP(A);
	for(int i = A.length; i > 1; i--){
		swap(A[i], A[0]);
		A.size--;
		max_heapify(A, 1);
	}
}
```


# Fila de Prioridade


MAXIMUM(S) devolve o elemento de S que tenha a maior chave.
![[Pasted image 20241007092630.png]]

INSERT(S, x) insere o elemento x no conjunto S. 
![[Pasted image 20241007092610.png]]

EXTRACT-MAX(S) remove e devolve o elemento de S que tenha a maior chave.
![[Pasted image 20241007092524.png]]

INCREASE-KEY(S, x, k) aumenta o valor da chave do elemento x até o novo valor k, que admite-se ser, pelo menos, tão grande quanto o valor da chave atual de x.
![[Pasted image 20241007092550.png]]
