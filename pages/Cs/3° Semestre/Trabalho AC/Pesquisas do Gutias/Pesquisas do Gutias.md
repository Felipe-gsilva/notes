### **velocidade de processamento**

O processamento em um sistema neuromórfico de uso quase comercial (ASIC/application specific inte

# Desempenho, Performance e Eficiência - PARTE 1

O desempenho de um sistema neural está atrelado a três aspectos importantes, normalmente associados, também, ao desempenho dos computadores Von Neumann. São eles:

- A eficiência energética
    - menos gasto por processo
    - menos energia dissipada
- A velocidade de processamento
- A confiança dos dados, baseada em:
    - Precisão dos bits após cada operação
    - delay durante a manipulação de dados

  

![[/Untitled 10.png|Untitled 10.png]]

## A velocidade de processamento

O processamento em um sistema neuromórfico de uso quase comercial (ASIC/application specific integrated circuit) pode ter velocidades padrões próximas a 320 gigaops por segundo, utilizando-se de, apenas, 0.6W de consumo. Essa alta taxa de processamento é, de fato, extrema, mas vem com alguns contrapesos.

## Problemas de precisão

A precisão de um sistema neural é uma questão muito importante para seu funcionamento. Dada a velocidade de processamento na pipeline, relacionada com a vasta quantia de transistores que executam simultaneamente uma grande quantidade distinta de operações, percebeu-se que, ao utilizar-se grandes quantias de dados em cada palavra endereçada, havia um aumento na perca de dados num quadro geral.  
Para evitar tais problemas e garantir a segurança da rotina executada, tende-se a utilizar numeros fixos de 8bits ao invés de floating points com 32bits.  

- Essa ideia, no entanto, vem com a perda de armazenamento local de dados, ja que as palavras se tornam muito menores e mais voláteis, tornando o princípio da localidade um pouco menos eficiente.

## A eficiência energética

O uso em geral de um computador neural pode ser medido em micro Watts (uW) por cada operação, tornando mais viável a verificação de um sistema global tanto quanto de apenas um componente. Essa ideia permite que o gasto total, como visto anteriormente, possa ser mesurado com alta efetividade, como observado no exemplo de 0,6W de consumo.

# Processador neuromórfico - PARTE 2

[https://www.researchgate.net/profile/Amirreza-Yousefzadeh/publication/342193391_NeuronFlow_a_neuromorphic_processor_architecture_for_Live_AI_applications/links/5eef3bc0299bf1faac690f2a/NeuronFlow-a-neuromorphic-processor-architecture-for-Live-AI-applications.pdf](https://www.researchgate.net/profile/Amirreza-Yousefzadeh/publication/342193391_NeuronFlow_a_neuromorphic_processor_architecture_for_Live_AI_applications/links/5eef3bc0299bf1faac690f2a/NeuronFlow-a-neuromorphic-processor-architecture-for-Live-AI-applications.pdf)

[https://arxiv.org/pdf/2203.07006](https://arxiv.org/pdf/2203.07006)

Os processadores neuromórficos são inspirados na arquitetura e funcionalidade das redes neurais biológicas, basicamente do cérebro humano. Esses processadores emulam o comportamento dos neurônios e sinapses, visando replicar baixo consumo de energia e alta eficiência computacional. No geral, a ideia nem sempre é perfeitamente alcançada, como visto anteriormente.

### Componentes lógicos:

- Neurônios
- Sinapses
- Motor de eventos

### Tipos de Processadores Neuromórficos

- **Processadores Neuromórficos Analógicos:**
    - Características: Utilizam circuitos eletrônicos analógicos para emular neurônios, oferecendo baixo consumo de energia através de tecnologia assíncrona.
- **Processadores Neuromórficos Digitais:**
    - Características: Consistem em muitos núcleos de processamento que se comunicam via Redes-em-Chip (NoCs) comutadas por pacotes. Os designs digitais evitem algumas limitações dos analógicos, mas tem alto consumo de energia e gargalos de memória.
- Exemplo Digital → NeuronFlow
    
    O neuronFlow é um tipo de arquitetura neuromórfica digital e tem suas características comuns aos demais tipos. São elas:
    
    - Núcleos de Processamento de Eventos → guarda o estado de eventos de 1024 neurônios
    - Neurônio → a parte computacional feita que forma as camadas de uma rede neural. Consegue receber input e enviar outputs com algoritmos e/ou dados específicos.
    - Sinapses → permite compartilhamento de informações entre os clusters de neurônios
    - Agregação de vizinhança → todo neurônio consegue receber e enviar dados de diversos neurônios vizinhos.
    - Esparsidade → alguns neurônios se tornam inúteis (tem peso zero) após o treinamento e são inutilizados.
    - virtualmente, funciona desta forma:
    
    ![[/Untitled 1 4.png|Untitled 1 4.png]]