Programação dinâmica: subdividir um problema de otimização nos quais temos estratégias mais simples de chegar em solução ótima.

A estratégia fundamental é armazenar a solução para cada um desses subproblemas em vez de recalculá-la. Veremos como essa ideia pode transformar algs de tempo péssimo em um tempo ótimo.

Os algoritmos gulosos se aplicam a problemas de otimização. A ideia é fazer cada escolha de maneira ótima local, resultando em um algoritmo mais rápido do que aquele obtido na prog dinâmica.

Veremos a análise amortizada também. Impõe um limite para o custo real da sequência inteira.

# programação dinâmica
armazenar os dados em tabelas para otimização

_ETAPAS_
1. caracterizar a estrutura de uma solução ótima
2. definir recursivamente o valor de uma solução ótima
3. calcular o valor de uma solução ótima, normalmente de baixo para cima
4. construir uma solução ótima