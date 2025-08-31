# Historia (Linha do tempo)
O primeiro computador a possuir recursos gráficos foir o Whirlwind I (1950), desenvolvido pelo MIT. Seguido por um sistema de monitoramente e controle de voos voltado para a defesa dos EUA.  No entanto, eles usavam a tecnologia de CRT (Cathode Ray Tube - TV de tubo), que foi descoberta em 1886. A seguir, uma linha do tempo:

1929: Fotograma - industria cinematográfica define o padrão de 24 FPS.

1927: Primeiro PC (Eniac)

1938: Proposta do CRT Colorido

1950: Laposky -> Primeiras obras de arte digital, usando um efeito de osciloscopio.

1955: surge o Sage de monitoramento aereo.

1959: surge o termo computacao grafica, criado por William Fetter da boeing.

1960: primerio computador comercial.

1961: space wars -> primeiro jogo usando comp. grafica.

1963: usando uma caneta grafica para desenhar.

1963: primiero filme do zajac.

1964: Boeing cria o primeiro modelo o corpo humano

1966: primero console -> odyssey | primeira empresa que cria animacoes -> MAGI

1970: tecnicas de CG como sombreamento e z-buffer.

1971: tomografia computadorizada

1972: ATARI

1975: CG se torna uma area academica 

1992: openGL

--- 

# Computação Gráfica
A computação gráfica é dividida em três vetores principais:
- Síntese de Imagens
- Processamento de Imagens: Visa melhorar ou alterar características visuais de imagens criadas. 
- Analise de Imagens: Obter características de componentes de uma imagem.

Veremos alguns conceitos dispersos a seguir, importantes para o entendimento de cg.
## Sistemas Gráficos
Sistemas gráficos podem ser representados:
- matricial (somente x e y -> tipo o paint) : nesta representação, a imagem é descrita por um conjunto de células em um arranjo espacial bidimensional. Cada célula representas os ditos *pixels*, que nada mais são do que pontos lógicos de representação.
- vetoriais:  nesta forma de representação, usam-se primitivas matemáticas para modelar os problemas e elementos a serem dispostos. Tais elementos são chamados de *primitivas vetoriais* e possuem seu conjunto de atributos e geometria.
    - utiliza de voxels (pixel com volume) para representação nos octantes.
    - Dispositivos 3d: impressora
    - Podemos modelar uma reta nesta representação da seguinte forma: $(x, y, z) = (P_2 - P_1)+t +P_1, \ 0 \leq t \leq 1$,  onde cada elementos de ponto corresponde as coordenadas no espaço de 0 a X, Y e Z delimitados.

## Dispositivos Graficos

### CRT (Cathode Ray Tube)
medida em pixel é uma unidade lógica e não física.
tamanho físico depende do dispostivo de projeção, depende da unidade minima de projeção. 
Esse valor em si é medido por `dot pitch` -> distancia entre 2 pontos de projeção é no máximo 0.28mm.

## LCD (liquid crystal display)
## Plasma 
Elotros emitem estimulos que passam os gases xeonio e neonio e alteram o estado deles entre gas -> plasma.
A liberacao da luz faz o fosforo brilhar.

---
# Colorimetria
Estudos das cores: primeiro sistema foi o `xyz`/`CIE`, atraves da resposta media de 20 individuos.

- Matiz (Hue): comprimento de onda dominante (Cor Pura)
- Saturação: Pureza da matiz (Quantidade que a cor está diluída em branco)
- Cromaticidade:

## Modelos Aditivos e subtrativos
### Adtitivo: projeção da luz
RGB
Canal R (8 bits) 0 - 255
Canal G (8 bits) 0 - 255
Canal B (8 bits) 0 - 255

Toda imagem usa os 3 canais com a quantidade de 0 a 255, onde cada canal se mistura formando branco com a maior quantdade de todos eles.

$f(x, y) = fr(x, y) + fg(x, y) + fb(x, y)$

HSV ou HSV (Hue - matiz, Saturation - saturacao e Value - luminancia)

### Subtrativos: absorção da luz
CMYK
