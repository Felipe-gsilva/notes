"Particle Systems—A Technique for Modeling a Class of Fuzzy Objects" -> primeiro artigo referente a modelagem de eventos chamados "nebulosos". Em geral, o modelo inova ao trocar a anterior representação de superfícies dos trabalhos previos. Usa-se de um oscilador estocástico. Esta técnica foi empregada no filme Star Trek II: The Wrath f Khan

https://www.youtube.com/watch?v=x8X44NRltMM - minuto 1.39

Este paper representa a primeira aparição de um sistema de particulas, alterando a representação de primitivas anterior, como poligonos com extremidades definidas, mas como nuvens de particulas primitivas que definem seu volume (futuramente a represetação Point Cloud também seria utilizada). Esse volume de particulas também não é uma entidade por si só, cada particula tem seu *lifetime* próprio com a passagem do tempo (esta modelada por uma série de oscilações estocásticas - randomicas | ou pseudo). 

Este projeto deriva de ideias prévias relacionadas aos videogames (provavelmente a primeira aplicação de cg em escala), como o grandissíssimo Evans e Sutherland Flight Simulator, que, alem de ser o projeto inventor dos frame buffers (lembrem do swap buffers do opengl), iniciou (primitivamente) o processamento de explosoes com um sistema simples de colisao e a tentativa de renderizar esse elemento "fuzzy" (como o fogo) mas sem a randomicidade esperada.

https://www.youtube.com/watch?v=iMpQuclk2vg - evans
https://s3data.computerhistory.org/brochures/evanssutherland.3d.1974.102646288.pdf - evans

# Fundamentacao deste projeto
Para renderizar esse sistema, o seguinte pipeline é seguido: (1) novas particulas sao introduzidas no sistema, (2) cada particula recebe seus atributos individualmente, (3) toda particula que exista no sistema depois de passar do seu tempo de vida, sao removidas; (4) as particulas restantes se movem baseadas nos seus atributos dinamicos e (5) a imagem do sistema é criada no frame buffer.

Este paper tratou alguns parametros dos sitemas de particulas:
- numero de particulas geradas (densidade) 
    - $NPartsf = MeanPartsf + Rand( ) × VarPartsf$ -> basicamente, media de particulas que o sistema deve ter somado a um um valor randomico de -1 a 1 * a variancia de particulas desejado. 
- variancia
    - o programador pode alterar a media atraves de alguma funcao qualquer, alterando o tamanho do volume.

Em geral, cada nova particula recebe:
1. posicao inicial
2. velocidade inicial (e direcao)
3. tamanho inicial
4. cor inicial
5. transparencia inicial
6. formato
7. tempo de vida (em frames)

problemas: (1) particulas nao podem interagir com outras superficies (2) so ha interacao de fato atraves de planos de projecao que limitam o crescimento das particulas. (3) toda particula eh um emissor de luz, que adiciona luz para as particulas internas e externas, nao sendo factivel com a realidade.
