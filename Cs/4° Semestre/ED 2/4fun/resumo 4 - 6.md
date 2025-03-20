## Aula 05 - Tries:

1. Árvores de Busca Digitais (Tries):

    Uma trie é uma árvore de busca onde o fator de subdivisão (número máximo de filhos por nó) é igual ao número de símbolos do alfabeto.
    A posição de um nó na árvore depende dos bits da chave, ao contrário das árvores AVL ou Rubro-Negras, que dependem da comparação das chaves.
    Tries são usadas para buscas rápidas, sendo eficiente em casos onde as chaves compartilham prefixos comuns.

2. Vantagens e Desvantagens:

    Vantagens: Implementação simples, pois não depende de operações de rotação, com sufixos compartilhando o mesmo caminho. Também é uma boa opção para chaves grandes e de tamanho variável.
    Desvantagens: O desempenho depende do tamanho das chaves. Para chaves com muitos bits, a trie pode ter grande profundidade, o que aumenta o custo de memória e busca.

3. Tempo de Busca:

    O tempo de busca em uma trie é proporcional ao tamanho das chaves. Chaves com sufixos comuns compartilham o caminho até a raiz, o que permite otimizações no espaço de armazenamento e no tempo de busca.

4. Exemplo de Trie:

    Na construção de uma trie, as chaves são inseridas letra por letra. Por exemplo, para armazenar as chaves "able", "abrahms", "adams", etc., uma árvore com ordem 26 (letras do alfabeto) será usada, com cada subdivisão representando uma letra.

5. Busca em Tries:

    A busca é realizada comparando os bits da chave em cada nível da árvore. O primeiro nível compara o bit mais à esquerda, o segundo nível o segundo bit, e assim por diante até o bit menos significativo.

6. Operações em Tries:

    Inserção: As chaves são inseridas na trie de acordo com os bits da chave. A árvore não mantém as chaves ordenadas, mas todas as chaves à esquerda de um nó são menores que as à direita.
    Remoção: A remoção de um nó pode ser complicada, pois pode desfazer a propriedade de compactação da trie. Em casos simples, se o nó é uma folha, ele é simplesmente removido, mas em casos mais complexos, o nó pode precisar ser substituído por um descendente.

	
## Aula 06 - Hashing:

1. Tabela Hash:

    Uma tabela hash é uma estrutura de dados que permite acesso rápido a elementos com base em uma chave, sendo composta por um array de "baldes" (buckets), onde os dados são armazenados.
    A chave é transformada em um índice através de uma função de hash, determinando onde o valor associado será armazenado ou encontrado.

2. Função de Hashing:

    A função de hashing (função de espalhamento) transforma a chave de busca em um endereço. Esse endereço é utilizado para armazenar ou recuperar registros.
    A função de hash deve distribuir as chaves uniformemente pelos buckets da tabela, minimizando colisões, ou seja, casos em que duas chaves diferentes resultam no mesmo índice.

3. Hashing Interno e Externo:

    Hashing Interno: Utilizado em memória principal, onde cada slot da tabela é um registro. Quando ocorrem colisões, pode-se usar listas encadeadas (endereçamento fechado) ou sondagem linear, quadrática e duplo hash (endereçamento aberto).
    Hashing Externo: Utilizado para armazenamento em disco. Cada slot é um bucket e as colisões são tratadas preenchendo o bucket.

4. Colisões:

    São situações em que duas chaves distintas resultam no mesmo índice. A solução para colisões envolve técnicas como:
        Listas Encadeadas: Onde vários elementos são armazenados no mesmo bucket.
        Endereçamento Aberto: Busca-se outro bucket disponível.
        Sondagem Linear: Procura sequencial por um slot vazio.
        Sondagem Quadrática e Duplo Hashing: Técnicas para espalhar melhor os dados e reduzir agrupamentos.

5. Exemplo de Função Hash:

    Um exemplo de função de hash pode usar os valores ASCII dos dois primeiros caracteres do sobrenome, multiplicá-los e utilizar os três dígitos menos significativos do resultado para gerar o endereço.

6. Métodos de Hashing:

    Divisão por um Número: A chave é dividida por um número, geralmente um primo, para obter um índice mais distribuído.
    Elevação ao Quadrado: Eleva-se a chave ao quadrado e usa-se os dígitos do meio como índice.
    Base Diferente: Converte a chave para outra base numérica e usa o valor convertido como índice.