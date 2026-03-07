# Agentes Inteligentes

Agente: entidade que percebe e atua em um ambiente 
Ambiente: parte do sistema que o agente não controla. 

O agente interage com o ambiente por meio de seus sensores e atuadores.

Os tipos de agentes incluem robôs, humanos e softbots (softwares).

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


## Espaço de estados 
Conjunto de todos os possíveis estados que podem ocorrer durante a resolução de um problema. Estados mudam conforme as ações.

## Conjunto de ações 
Conjunto finito de ações que alteram dentre os estados do espaço de estados.
- Teste de objetivo: se estado = estado objetivo

Para encontrarmos o plano ótimo, criamos uma árvore com todos os estados percorridos e usamos um algoritmo de busca para isso.

## Tipos clássicos de busca 

- BFS 
- DFS 

## Heuristicas de busca 
faz uso do conhecimento especifico do problema para encontrar soluções 

ideia-chave: uso de função de avaliação, f(n) que retorna uma estimativa do valor do nó n (ela esitma para chegar até o nó n). Espera-se expandir o nó desejado que ainda não foi expandido.

### busca gulosa

usando a heurística "distância em linha reta"

### A*

