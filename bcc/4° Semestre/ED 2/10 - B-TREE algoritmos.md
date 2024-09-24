```c
struct page {
	int keycount;      // contador
	char key[MAX]      // chaves atuais
	int child[MAX + 1] // RRNS dos filhos
}

// page.child[i] = filho a esquerda
// page.child[i+1] = filho a direita
```
## representação lógica:
page 2

| 2   | D        H       K | 0      3      8       5 |
| --- | ------------------ | ----------------------- |

page 3

| 3   | E       F         G | NULL NULL NULL |
| --- | ------------------- | -------------- |
| 0   | B                   | NULL NULL NULL |

## detalhes impl
__	importante salvar no header o RRN da raiz.
__	se o filho é **null** escreva o ponteiro como um * 


---
# Algoritmos
ex: escreva o algoritmo que busca em uma b-tree
# busca
```c
#define ROOT 2 // mudar para o header record

typedef struct page {
	int keycount;      // contador
	char key[MAX]      // chaves atuais
	int child[MAX + 1] // RRNS dos filhos
} page;

page search (RRN, KEY, FOUND_RRN, FOUND_POS) {
	if RRN == null 
		return NULL;
	page = load_page(RRN); 
	POS = search_key(page, KEY);
	if(POS == FOUND) { // se b está nessa pagina, POS = FOUND, se tiver na esquerda, ou n existir, POS = NOT_FOUND
		FOUND_RRN == RRN;
		FOUND_POS == POS;
		return page;
	}
	return search(page->child[POS], KEY, FOUND_RRN, FOUND_POS);
};

int search_key(page, KEY) {
	// tem que melhorar isso daqui
	for(int i = 0; i < PAGE_MAX; i++) {
		if(page.key[i] == KEY)
			return i;
	}
	return NULL; // mudar retorno
}

```
# Inserção
busca se a chave atual existe na árvore até chegar no nó folha em que ela deveria estar

## fases
- search step
- recurisve call
	- mover a operação ao niveis inferiores (ultima página possivel)
- inserção
	- split 
	- promotion 
- tipos de retorno
	- PROMOTION (1)-> quando uma inserção é feita e uma chave é promovida
	- NO PROMOTION (0)-> quando não há promoção (nó com espaço livre)
	- ERROR (-1) -> quando a chave em si já existe (retornar o indice da chave primária)
- variáveis locais
	- page: pagina atual
	- newpage: pagina nova criada
	- pos: posição da página na qual a chave já ocorre ou deveria ocorrer
	- P_B_KEY: chave promovida do nível inferior para ser inserida em page;
	- P_B_RRN:
		- RRN promovido do nivel inferior para ser inserido em page
		- filho a direita
```c
int insert (CURRENT_RRN, KEY, PROMO_KEY, PROMO_RIGHT_CHILD) {
	if CURRENT_RRN == null {
		PROMO_KEY = KEY;
		PROMO_R_CHILD=NULL;
		return PROMOTION;
	}
	page = load_page(CURRENT_RRN);
	POS = search_key(page, KEY);

	if(KEY = page.key[POS]) {
		log("ERROR: CHAVE JA EXISTE");
		return ERROR;
	}
	RETURN_VALUE =  insert(page.child[POS], KEY, P_B_RRN, P_B_KEY)
	if (RETURN_VALUE == NO PROMOTION || RETURN_VALUE == ERROR)
		return RETURN_VALUE;
	if (page_key_count(page) < KEY_MAX)
		// inserir P_B_KEY e P_B_RRN em page;
		return NO_PROMOTION;
	split(P_B_KEY, P_B_RRN, page, PROMO_KEY, PROMO_R_CHILD, NEWPAGE);
	// escrever page no RRN atual;
	// escrever new page no arquivo na posição PROMO_R_CHILD
	return PROMOTION;
}
```
## split
representa o tratamento de overflow causado por uma nova página
```c
void split(P_B_kEY, P_B_RRN, PAGE, PROMO_KEY, PROMO_R_CHILD, NEWPAGE) {
	// cria uma nova página (NEWPAGE)
	new_page();
	// distribui as chaves entre page e newpage
	int mid = (int)ORDER/2;
	// determina qual chave e qual RRN serão promovidos
	/*
		PROMO_KEY;
		PROMO_R_CHILD;
	*/ 
}
```
## procedimento driver 
rotina inicializadora e de tratamento da raiz
- abre ou cria o arquivo de indice (arvore-b)
- identifica ou cria a página da raiz
- lê chaves para serem armazenadas na b-tree e chama insert de forma apropriada
- cria uma nova raiz quando insert particiona a raiz atual

```c
void procedure() {
	if arquivo com árvore-b existe {
		abrir arquivo
	}
	else criar arquivo e colocar a primeira chave na raiz
	// recupere RRN da pagina raiz e armazene em root
	// leia uma chave e armazene em key
	while key existe {
		if(insert(ROOT, KEY, PROMO_R_CHILD, PROMO__KEY) == PROMOTION){
			crie uma nova raiz (com a promo key), l_child=root atual, r_child=promo_r_child
			faça root igual ao rrn da novaa pagina raiz
		}
		leia a proxima chave e armazene em key
	}
	escreva no arquivo a ultima raiz
	feche o arquivo
}
```
# Propriedades
- todas as folhas estão no mesmo nível
- toda página, exceto a raiz tem no minimo [m/2] descendentes
- uma página n folha que possui k filhos tem k-1 chaves

complexidade da árvore:
$N+1 \geq 2 x \lceil \frac{m}{2}\rceil^{d-1} \implies d \leq 1 + \log_{\lceil \frac{m}{2}\rceil}((N+1)/2)$
# remoção
eliminação 
caso 1: eliminar uma chave de uma página folha. 
- Solução, chave é retirada e os registros internos à página são reorganizados.

caso 2: uma chave fora da folha
- trocar com a sua sucessora imediata (menor da direita ou maior da direita) que está numa folha, deleta o que foi pra folha, e deixe o sucessor imediato na pagina de cima

caso 3: eliminação causa underflow e podemos redistribuir
- solução redistribuição
- procura-se uma página irmã que contenha mais chaves do que o minimo (se existir, redistribuiremos)
- juntamos as 2 páginas, escolhemos a chave mediana da junção e distribuimos metade pra cada, promovendo essa chave mediana e colocando a chave do pai trocada com a mediana

caso 4: ocorre underflow e a redistribuição não pode ser aplicada
- não existem chaves suficientes nos irmãos. 
- solução: concatenação
	- combina-se o conteudo das 2 páginas.
	- combinamos as 2 páginas, pegamos o maior deste nova e o promovemos

caso 5: underflow no pai, como consequencia da concatenação
- solução: underflow se propaga pra cima. Temos então, que concatenar recursivamente quando possível

caso 6: quando o underflow ocorre na raíz (raiz < 1 chave)
- concatenar os nós filhos
## passos
1. se a chave não estiver numa folha, troque-a com a sua sucessora imediata
2. elimine a chave da folha
3. se a página continuar com o número mínimo de chaves, fim.
4. se a página tem uma chave a menos q (m/2) -1, verificamos as páginas irmãs a esquerda e depois da direta
	1.  se uma delas tiver mais q o numero minimo de chaves, redistribua
	2. se não, concatene com a página e a chave separadora do pai
5. se ocorreu concatenação aplique os passos de 3 a 6
6. se a ultima chave da raiz for removida, alterar a raiz e a altura diminui
![[B_TREE_REMOVAL]]
