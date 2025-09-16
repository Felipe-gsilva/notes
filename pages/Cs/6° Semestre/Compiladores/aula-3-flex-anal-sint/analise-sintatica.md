> aula referente ao cap 4.1 e 4.4 do livro

# Análise Sintática
![[Pasted image 20250916171035.png]]

Entrada: Cadeia de tokens representando o programa fonte e verifica se a cadeia em si pertence a linguagem gerada pela gramatica.

Ele deve ser projetado para emitir mensagens de erros de uma forma inteligível e se recuperar deles, em certas ocasiões.

Aqui, devemos estruturar a gramatica de fato, partindo, naturalmente, de uma _keyword_ definida, i.e, *while* ou *int*, assim, os proximos lexemas a serem aceitos devem se basear nessa indicação.

Utilizaremos um PDA (*push-down automata*) para aceitarmos a gramatica, devido a sua "memoria" (pilha). Assim, podemos aceitar uma sequencia de tokens como `int a = 5;` ou não, ja que ele olha todos os lexemas.

O analisador sintático interage com a tabela de símbolos, adicionando, por exemplo, `tipo`, `argumentos`, etc.

Saída: Gera uma arvore de derivação (arvore sintática) como saída.

## Tratamento de erro

Precisa-se tratar erros corretamente e existem diversas maneira de o fazer. Devemos atrasar a _parada_ do programa, apenas marcando erros e os informando ao final da analise (se não for critico); O compilador pode, por exemplo, parar essa emissão de mensagens em caso de um *threshold* de erros seja alcançado (e.g 50). 

Estratégias podem ser:

### Recuperação no modo panico
// livro
### Recuperação em nível de frase
// livro
### Produções de Erro 
// livro
### Correção Global
// livro

# Tipos de Analise Sintática
- Descendente
- Ascendente
## Descendente (top down)
> "Na analise sintatica Descendente, inicia-se o processo pelo simbolo S e chega-se à cadeia."

constroi a arvore de derivação para a cadeia de cima para baixo, da raiz para as folhas, criando os nos da arvore em pré-ordem (DFS). Pode ser recursiva ou nao recursiva.


## Ascendente (bottom up)
> "Na análise ascendente, tenta-se construir a árvore de derivação para uma sentença $w$ a partir dos símbolos de $w$ (folhas), fazendo reduções (substituir o lado direto de uma regra pelo seu lado esquerdo) até obter-se o símbolo inicial S".

constroi a arvore de redução ao invés de derivação para a cadeia de baixo para cima, das folhas para a raiz.

## Diagramas de Transicao para Analisadores Sintaticos Preditivos

> [!note] Caderneta
> Visto no caderno

## Construcao do ASDR (analisador sintatico descendente recursivo)
- construir as rotinas que implementam cada um dos diagramas de transição da gramatica referente.

## Extra 

como implementar a tabela de simbolos?
- pode ser uma AVL, com busca consideravelmente rapida (em $O(log(n))$);
- qualquer arvore balanceada;
- tabela hash (prioridade - se bem espalhada) $(O(log(1)))$.

