# von Neumann vs Neuromorphic

## System level

- O sistema da arquitetura de Von Neumann é dividido em unidades principais rígidas, físicamente separadas como a unidade de memória (UM), unidade lógica-aritmética (ULA), unidade de controle (UC) e vias de dados.
- Essa separação cria um gargalo temporal e energético conhecido como gargalo de von Neumann.
- Na arquitetura neuromórficas os vários elementos computacionais são misturados e o sistema é dinâmico.
    - Baseado em um processo de “Aprendizado” onde os diversos elementos do sistema mudam e se reajustam dependendo do estímulo recebido

## Device Level

- A computação clássica é baseada em transistores, resistores, capacitores, indutors e conexões de comunicações
    - **Vantagens:** velocidade, tamanho e operating range (?)
    - **Desvantagens:** consumo de energia, design e funcionalidade rígida, baixa tolerância a defeitos, conectividade limitada.
- Na computação neuromórfifca, são usado “neurônios” que possuem um corpo (soma), sinapses, axônios e dentritos que são adaptáveis, tolerante a erros e permitem conexões complexas.

## Performance

- Mesmo que os componentes individuais da arquitetura de von Neumann demonstrem maior performance, o sistema como um todo possui uma funcionalidade muito mais reduzida.
- Sistemas neuromórficos são superiores em outras caracterísitcas:
    - possuem uma dissipação de potência muitíssimo maior

# Neuron Models

- O modelo de rede neural usado define quais componentes formam a rede neural, como esse componentes operam e como eles interagem.
- Durante a definição do model é necessário também definir qual modelo usar para cada componente
- O modelo escolhido devem ser motivado pela área de aplicação

**Exemplos:**

1. Em um dispositivo neurmórfico com o objetivo de simular cérebros biológicos para estudos de neurociência em uma escala mais rápida do que a possível com a arquitetura von Neumann: um modelo biologicamente plausível
2. Se a aplicação é uma de reconhecimento de imagem que requer alta acurácia: Um modelo que utiliza redes convolucionais

- Os modelos variam de predominantemente biológicamente inspirados para predominantemente computacionalmente motivados.
    - Esse último é mais inspirado por ANN do que cérebros biológicos

## Modelos de neurônios

- Um neurônio biológico é composto por um corpo celular, axônios e dentritos:
    - O axônio transmite informação do neurônio e é onde o neurônio transmite sua saída
    - Os dentritos transmite informações para o corpo celular e é onde o neurônio recebe sua saída
    - A junção entre o axônio de um neurônio e o dentrito de outro neurônio é chamado de sinapse
    - O potencial de voltagem de um neurônio pode superar um limite e causar a ativação do neurônio
- O comportamento de típico de um neurônio é de acumular potencial de voltagem causado por receber sinais de outro neurônios por sinapses até ultrapassar um limite
    - Causando o neurônio a disparar o seu sinal e afetar as cargas de outro neurônios por sinapse.
- A maioria dos modelos implementam esse comportamento de acumulação de carga e disparo através de mecanismos diferentes.

1. **Biologicamente plausíveis**: Modelam explicitamente o tipo de comportamento que é observado em sistemas neurais biológicos. O modelo mais popular é o Hodgkin-Huxley model. Que é um modelo neurônio relaticamente complexo que utiliza equações diferenciais não lineares de quatro dimensões para descrever o comportamento de transferência de íons entre neurônios. Um modelo mais simples é o Morris Lecar que reduz o modelo para equações não lineares de duas dimensões.
2. **Biologicamente inspirados:** Tentam replicar o comportamento de sistemas neurais biológicos mas não necessariamente de maneira biologicamente plausível. Existem uma variedade de modelos simplificados do Hidgkin-Huxley que foram implementados em hardware como o Fitzhugh-Name e o Hindmarsh-Rose. Tendem a ser mais simples computacionalmente e em número de parâmetro permitindo uma implementação em hardware mais energeticamente e financeiramente além de simplificar o processo de treinamento.
3. **Neuron+Other:** Modelam neurônios em conjunto de outro componente biologicamente inspirado que não comumente incluídos em outro modelos neuronais. Normalmente contém um nível de detalhe biológico muito maior que os outros.
4. **Integrate-and-fire (I&F):** Uma categoria mais simples de modelos neurônios spiking. Tendem a variar em complexidade, como por exemplo o modelo Izhikevich. Os modelos mais simples mantém o nível de carga estável enquanto implementações mais complexas a perda dessa carga. Também podem utilizar técnicas não lineares. Existem também implementações digitais que utilizar automatas celulares.
5. **McCulloch-Pitts:** Modelos que derivam do original McCulloch-Pitts, seguindo a seguinte equação. É uma implementação mais tradicional de neurônios, como por exemplo o perceptron.

## Modelos de sinapses:

- Também existe um foco na implementação de sinapses em particular com pesquisas com enfoque nela.
- Podem ser divididas em biologicamente inspiradas que incluem sinapses baseadas em spikes e implementações tradicionais de ANN, como as redes neurais feed-forward.
- É o elemento mais abundante em um rede neural e onde a maioria do custo e área de um chip se encontra.
- A maioria da pesquisa é tipicamente focada em otimizar as implementações de sinapses.
- Tendem a ser simples a menos que estejam tentando modelar explicitamente um comportamento biológico.
- Uma implementação popular complexo é o mecanismo de plasticidade.
    - Faz com a força ou o peso dele um neurônio mude com o tempo, inspirado na neuroplasticidade de cérebros biológicos.
- Modelos mais biologicamente inspirados tendem a modelas explicitamente as interações quiímicas da sinapses, incluindo íons e neurotransmissores. Superando até mesmo os deltahes de modelos de neurônios como Hodgkin-Huxley.

## Modelo de redes

- Descrevem como os diferentes neurônios e sinapses são conectados e como eles interagem.
- Um dos fatores é a inspiração biológica, a complexidade do neurônio e modelos de sinapses e a topologia da rede neural.
- Algumas restrições são o hardware que impede a possibilidade de aplicar certas conectividades e a topologia das redes.
- Outra restrição é a aplicabilidade de algoritmos de aprendizados diferente
- A maioria da implementações de redes neurais em hardware usam spiking, existindo uma grande variedade dos mesmo.
    - Essa popularidade é devido a sua natureza event-driven e eficiência energética em relação aos outros sistemas.
- A implementação mais popular é as redes neurais feed-forward incluindo MLP e ELM
- Redes neurais recorrentes são aquelas que permitem por ciclos na sua rede com níveis diferentes de conectividades