**Objetivo:** permitir busca sequencial e direto.

Pensada em ranges. Utilizada em muitos sistemas de arquivos.
- Conjunto de indices, organizado igualmente como a _B_TREE_
- Sequence Set: lista encadeada que liga as folhas da b-tree (blocos de tamanho fixo ordenados pelas chaves). 

### props
1. Os nós internos não contém dados secundários dos registros, apenas cópias das chaves e servem só como referência para o percurso. Em outras palavras, abrigam apenas separadores de chave.
2. são utilizados blocos para armazenar os dados de fato, assim, o tamanho do bloco se difere da ordem da árvore.

podemos fazer a maior parte das exclusões e inclusões sem alterar os índices, apenas no conjunto sequencial.

# Operações
Busca por range: 
- encontra o primeiro bound do range seguida por uma busca linear até o limite $[4, 7]$.
- só se pode ter certeza que um registro foi encontrado quando se chega na folha.
- se chave_atual > chave_buscada, descemos pelo ponteiro da esquerda
- se chave_atual <=  buscada, descemos no ponteiro à direita.

## Inserção:
- no overflow do indice interno = igual a b-tree normal
- no overflow do bloco, subimos só uma cópia da chave mediana do novo nó pai.
