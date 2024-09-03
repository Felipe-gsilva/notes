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

| 3   | D        H       K | 0      3      8       5 |
| --- | ------------------ | ----------------------- |
## detalhes impl
__	importante salvar no header o RRN da raiz.
__	se o filho é **null** escreva o ponteiro como um * 


---
# Algoritmos
ex: escreva o algoritmo que busca em uma b-tree
```c
typedef struct page {
	int keycount;      // contador
	char key[MAX]      // chaves atuais
	int child[MAX + 1] // RRNS dos filhos
} page;

page search () {


};
```