"Particle Systems—A Technique for Modeling a Class of Fuzzy Objects" -> primeiro artigo referente a modelagem de eventos chamados "nebulosos". Em geral, o modelo inova ao trocar a anterior representação de superfícies dos trabalhos previos. Usa-se de um oscilador estocástico. Esta técnica foi empregada no filme Star Trek II: The Wrath f Khan

https://www.youtube.com/watch?v=x8X44NRltMM - minuto 1.39

Este paper representa a primeira aparição de um sistema de partículas, alterando a representação de primitivas anterior, como polígonos com extremidades definidas, mas como nuvens de partículas primitivas que definem seu volume (futuramente a representação Point Cloud também seria utilizada). Esse volume de partículas também não é uma entidade por si só, cada partícula tem seu *lifetime* próprio com a passagem do tempo (esta modelada por uma série de oscilações estocásticas - randômicas | ou pseudo). 

Este projeto deriva de ideias prévias relacionadas aos videogames (provavelmente a primeira aplicação de cg em escala), como o grandessíssimo Evans e Sutherland Flight Simulator, que, além de ser o projeto inventor dos frame buffers (lembrem do swap buffers do opengl), iniciou (primitivamente) o processamento de explosões com um sistema simples de colisão e a tentativa de renderizar esse elemento "fuzzy" (como o fogo) mas sem a aleaotiriedade esperada.

https://www.youtube.com/watch?v=iMpQuclk2vg - evans e sutherland
https://s3data.computerhistory.org/brochures/evanssutherland.3d.1974.102646288.pdf - evans e sutherland

# Fundamentação
Para renderizar esse sistema, o seguinte pipeline é seguido: (1) novas partículas são introduzidas no sistema, (2) cada partícula recebe seus atributos individualmente, (3) toda partícula que exista no sistema depois de passar do seu tempo de vida, são removidas; (4) as partículas restantes se movem baseadas nos seus atributos dinâmicos e (5) a imagem do sistema é criada no frame buffer.

Este paper tratou alguns parâmetros dos sistemas de partículas:
- numero de partículas geradas (densidade) 
    - $NPartsf = MeanPartsf + Rand( ) × VarPartsf$ -> basicamente, media de partículas que o sistema deve ter somado a um um valor randômico de -1 a 1 * a variância de partículas desejado. 
- variância
    - o programador pode alterar a media através de alguma função qualquer, alterando o tamanho do volume.

Em geral, cada nova partícula recebe:
1. posição inicial
2. velocidade inicial (e direção)
3. tamanho inicial
4. cor inicial
5. transparência inicial
6. formato
7. tempo de vida (em frames)

problemas: (1) partículas não podem interagir com outras superfícies (2) só há interação de fato através de planos de projeção que limitam o crescimento das partículas. (3) toda partícula eh um emissor de luz, que adiciona luz para as partículas internas e externas, não sendo factível com a realidade.
