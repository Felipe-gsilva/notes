> aula referente ao cap 4.1 e 4.4 do livro

# Análise Sintática

Entrada: Cadeia de tokens representando o programa fonte e verifica se a cadeia em si pertence a linguagem gerada pela gramatica.

Ele deve ser projetado para emitir mensagens de erros de uma forma inteligivel e se recuperar deles, em certas ocasioes.

Aqui, devemos estruturar a gramatica de fato, partindo, naturalmente, de uma _keyword_ definida, i.e, *while* ou *int*, assim, os proximos lexemas a serem aceitos devem se basear nessa indicacao.

Utilizaremos um PDA (push-down automata) para aceitarmos a gramatica, devido a sua "memoria" (pilha). Assim, podemos aceitar uma sequencia de tokens como `int a = 5;` ou nao, olha todos os lexemas.

O analisador sintatico interage com a tabela de simbolos, adicionando, por exemplo, `tipo`, `argumentos`, etc.

Saida: Gera uma arvore de derivacao (arvore sintatica) como saida.

## Tratamento de erro

Precisa-se tratar erros corretamente e existem diversas maneira de o fazer. Devemos atrasar a _parada_ do programa, apenas marcando erros e os informando ao final da analise (se nao for critico); O compilador pode, por exemplo, parar essa emissao de mensagens em caso de um *threshold* de erros seja alcançado (e.g 50). 

Estrategias podem ser:

### Recuperacao no modo panico
// livro
### Recuperacao em nivel de frase
// livro
### Producoes de Erro 
// livro
### Correcao Global
// livro

# Tipos de Analise Sintatica
- Descendente
- Ascendente
## Descendente (top down)
> "Na analise sintatica Descendente, inicia-se o processo pelo simbolo S e chega-se à cadeia."

constroi a arvore de derivacao para a cadeia de cima para baixo, da raiz para as folhas, criando os nos da arvore em pre ordem (DFS). Pode ser recursiva ou nao recursiva.


## Ascendente (bottom up)
constroi a arvore de derivacao para a cadeia de baixo para cima, das folhas para a raiz.

> "Na análise ascendente, inicia-se pelas folhas da árvore de derivação até chegar em S."

## Diagramas de Transicao para Analisadores Sintaticos Preditivos

> [!note] Caderneta
> Visto no caderno

## Construcao do ASDR (analisador sintatico descendente recursivo)
- construir as rotinas que implementam cada um dos diagramas de transicao da gramatica referente.

## Extra 

como implementar a tabela de simbolos?
- pode ser uma AVL, com busca consideravelmente rapida (em $O(log(n))$);
- qualquer arvore balanceada;
- tabela hash (prioridade - se bem espalhada) $(O(log(1)))$.

