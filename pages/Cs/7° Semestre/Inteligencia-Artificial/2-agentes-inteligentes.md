# Agentes Inteligentes

Agente: entidade que percebe e atua em um ambiente 

Ambiente: parte do sistema que o agente não controla, mas interage.

O agente interage com o ambiente por meio de seus sensores e atuadores e podem ser do tipo robôs, humanos e softbots (softwares) e etc.

Quando o agente é capaz de desempenhar "o que é correto" para atingir-se um certo objetivo, o chamamos de racional. No contexto da IA, agir de forma correta é entendido como realizar com sucesso uma dada tarefa.

## Avaliação de sucesso
Exemplo Melhor caminho para um robo:
- Caminho A -> curto, mas as vezes congestionado;
- Caminho B -> médio, mas normalmente livre;
- Caminho C -> longo mas sempre livre;

O sucesso do agente se dá somente ao fato dele chegar no local. Podemos, no entanto, usar o tempo como métrica de avaliação.

Agora, com melhor precisão, o agente racional é aquele que realiza ações que maximizam sua função utilidade (U), a qual descreve os objetivos do agente.

## Exemplos

1. Sistema de recomendação (streaming)
U = Relevância X Probabilidade (do usuário assistir)
Maximizar a satisfação do usuário sugerindo as produções mais relevantes, considerando seu histórico.

2. Chatbots
U = Relevância_da_resposta - Tempo_de_processamento

3. Modelos de Machine Learning
U = -Erro ou $\frac{1}{Erro}$
Objetivo: Maximizar o erro negativo (acerto) da predição do modelo.

4. Pacman 
Diante de um objetivo a ser alcançado, um agente deve buscar um plano.
Plano: sequência de ações que o agente deve executar em prol do objetivo. Partindo de um estado inicial e chegando no estado objetivo.

- Espaço de estados: Conjunto de todos os possíveis estados que podem ocorrer durante a resolução de um problema. Estados mudam conforme as ações.
- Conjunto de ações: Conjunto finito de ações que alteram o estado atual dentre os estados do espaço de estados.
- Teste de objetivo: se estado = estado objetivo
- Fronteira (ou borda): Trata-se do conjunto de nós folha da árvore de busca que estão disponíveis para serem expandidos em um dado momento

Para encontrarmos o plano ótimo, criamos uma árvore de busca com todos os estados percorridos e usamos um algoritmo de busca nela, visando encontrar um plano (caminho) que nos leve ao estado final (objetivo) que maximize a função utilidade.


## Algoritmos clássicos de busca 

Podem ser avaliados quanto a: (i) completude: um algoritmo é dito completo se encontrar solução válida; (ii) otimidade: se otimiza a função utilidade. VVeremos exemplos de busca em árvores abaixo:

### Busca Cega (Não informada)
- BFS: busca em largura (usa um fila como auxiliar). É um algoritmo completo e ótimo se o custo for unitário. Porém, depende de muita memória.
- DFS: busca em profundidade (usa uma pilha como auxiliar - pode ser a stack de recursão). Utiliza pouca memória mas não é completo, pode cair em loops.
- DFS Limitada: impõe um limite $L$ de profundidade permitida.
- IDDFS: busca em profundidade iterativa: Realiza buscas em profundidade limitada repetidas vezes, aumentando o limite L gradativamente a cada ciclo.

### Busca Informada (Com Heuristicas)
Utiliza conhecimento prévio e específico do problema para tomar decisões mais eficientes de qual caminho seguir.

Função de Avaliação: a busca informada utiliza uma função de avaliação $f(n)$ para estimar o custo de chegar em dado nó $n$, permitindo a escolha do nó com menor estimativa de custo.

Função Heuristica: é a estimativa em si, extraida da lógica do problema.

- Busca Gulosa: tornar a heurística $h(n) = f(n)$, obviamente não é ótimo, pois usa apenas a estimativa de custo, sem confirmação real.


#### Busca A*

É um dos algoritmos de busca informada mais clássicos e eficientes. A ideia dele é evitar expandir caminhos que já se mostraram caros. 

É definido pela função: $f(n) = g(n) + h(n)$, onde:

- $g(n)$: É o custo real do caminho percorrido desde o estado inicial até o nó atual.
- $h(n)$: É a heurística.

A busca A* depende que a heurística seja admissível, ou seja, quando ela é otimista (nunca superestima o custo real). Sua desvantagem é precisar manter todos os nós em memória, mas como minimiza-os, serão (provavelmente) poucos nós no conjunto residente.
