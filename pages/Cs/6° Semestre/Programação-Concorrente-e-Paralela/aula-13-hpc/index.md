### introdução

>um bilhão de operações de ponto flutuante por segundo (1 Gflop) é rápido o suficiente? 

há milhares de ano (quando o aleardo fez o slide), seria

#### previsão meteorológica pelo cubo

base do cubo é a região da previsão e a altura é a altitude 

considerando uma área de 20 milhões de km², como sendo um cubo de altitude de 20km, com pontos de discretização a cada 1km, teríamos aproximadamente 4x10⁸ pontos 

no final, teremos $10^{14}$ de operações no total, no nosso computador de 1 Gflop, levaria cerca de 10⁵s

comparando com um outro pc com 4 Gflop por thread (tendo 2 threads por núcleo), levaria 25x10³

já com o jesus dos computadores,(Threadripper) de 634 Gflops, 96 núcleos, 192 theads... faz em menos de 3 minutos (isto com os 96 núcleos no seu máximo, operando em paralelo, em condições ideais)

como implementar este estado ideal?

### paralelismo generalizado

suponha uma máquina com 200 Gflops e usarmos o comando

```
for (i = 0; i <DuzentosBi); i++)
	z[i] = x[i] + y[i];
```

para fazer isto 200 bi de vezes, se faz 600 bi de acessos na memória

com cada acesso, ocorrendo na velocidade de luz e distancia medida $d$ (entre CPU e memória)

$d$ = v / n° de acesso = 0,5mm

diam = 2 * d = 1mm

.... é impossível, para cada posição de memória teria que ocupar um espaço de 10 átomos...

### casos de uso de supercomputador

coisa pra cacete
- pampers
- pringles
- aerodinamica
- data mininig
- ...

### arquitetura de computadores

von neumann

classificação de flynn

### multicomputadores x multiprocessadores

UMA -> uniform memory acess
- todos os dados tem tempo de acesso unforme para todos os processadores

NUMA -> not uniform memomry access
- cada chip tem sua memória, por exemplo: chip1 tem memoria1 mais próxima, caso va acessar memoria2, o tempo de acesso será diferente

COMA -> cache only memory access
- o acesso aos dados é feito considerando a amemória local como memória cache

### timeline

fez uma timeline de supercomputadores

SIMD (maquinas massivamente paralelas)

### top 500

no brasil, a petrobras domina 







