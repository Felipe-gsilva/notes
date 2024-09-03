## Árvore bin de busca
Da pra criar uma arvore de busca binária em um arquivo, com os **Records** recebendo um ponteiro a direita e a esquerda do próximo registro, assim como uma chave própria. 
(key, rrn-left, rrn-right). O que isso gera é um desbalanceamento.
![[Árvore Binária de Busca - files]]
## AVL
temos a garantia com O(log(n)). Problema:
- se as chaves estão no arquivos, há muitos acessos desnecessários.

# Árvore Binária Paginada (Paged Binary Tree)

Cada 'página' é armazenada em um bloco, podendo conter um numero grande de Records, ou seja, é uma árvore *blocada*.

## Página:
Conjunto de setores logicamente contíguos no disco. Uma pagina é um grupo de $n$ records. 

## Problema da construção top-down
Construir uma arvore paginada é relativamente simples se temos todo o conjunto de chaves antes de iniciar a construção. Sabemos que temos que começar com a chave do meio.
Porém, se for em sequência aleatória.

A solução é uma árvore B (B-TREE).

---
# B-TREE

## Propiedades 
- completamente balanceadas 
- Não são binárias.
- Conteúdo de uma página não é mantido em uma árvore.
- Construção bottom-up
	- folhas -> raiz
- chaves **erradas** não são mais alocadas no no raiz. 
- cada página (ou nó) é formada por uma sequencia ordenada de chaves e um conjunto de ponteiros. 
- não existe uma árvore explicita dentro de uma página
- ordem = numero de chaves + 1
- Os nós folhas não possuem filhos.

Estrutura de um nó 
Registro de tamanho fixo -> RRN

é uma árvore com vários filhos, apenas.

# Inserção 
- sempre realizada nos nós folhas (a busca binaria por uma chave inexiste termina sempre no no folha)
- ordem previamente definida
- **casos**
	- inserção em B-TREE vazia
		- criação e preenchimento em um nó (raiz)
		- demais chaves são inseridas até a capacidade do nó
		- tem que ser ordenadas na inserção
	- overflow no nó raiz
		- 1. particionamento do no (split)
			- nó original = nó original + novo nó
			- split 1-to-2
			- as chaves são distribuídas uniformemente nos 2 nós
			- chaves do nó original + nova chave
		- 2. criação de uma nova raiz (efeito bottom-up) 
			- raiz = pagina 2 -> left=pagina 0, right=pagina 1
		- 3. pegar a nova chave separadora
			- a primeira chave separadora (ou a chave final da primeira página, ou a primeira chave da segunda página).
			
![[B-TREE example]]

# Inserção em nós folhas
1. passo 1 ->pesquisa binária, inserção sempre nas folhas
	- até encontrar o nó folha certo
2. inserção em nó num lugar disponível
3.  inserção em nó cheio (overflow)
	1. fazer um split (criar um novo nó e inserir a metade dele no novo nó)
	2. promoção -> escolher a primeira chave do novo nó para ser a separadora no nó pai.
	3. ajuste do nó pai para apontar para o novo nó
![[B-TREE ex2]]

O arquivo que contém a árvore-B é um arquivo com registros de tamanho fixo, sendo que cada registro contém uma página da árvore.