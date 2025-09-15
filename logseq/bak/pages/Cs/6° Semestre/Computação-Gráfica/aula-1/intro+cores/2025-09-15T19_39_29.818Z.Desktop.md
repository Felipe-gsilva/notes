# Aula 1 - Comp. Grafica

- Dispositivos e sistemas graficos (matricias e vetorias)
- Transformacoes geometricas no plano e no espaco
- Rasterizacao de primitivas
- Coordenadas homogeneas 
- Composicoes 
- Tecnicas ...

Prova 23/10
Seminarios 3 seguidos

Media = (P + S + T) / 3

# Historia
1886 - Inicio do desenvolvimento de CRT (Cathode Ray Tube - TV de tubo)
-> Projeção 

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

# Comp Grafica
- Sintese de Imagens
- Processamento de Imagens
Visa melhorar ou alterar caracteristicas visuais de imagens criadas. 
- Analise de Imagens
Obter caracteristicas de componentes de uma imagem.

## Sistemas Graficos
Comecaremos com OpenGL (Graphics Library). A interface entre o software e o hardware grafico é feita através de procedures e funções.
- matricial (somente x e y)
- vetoriais (coordenadas x, y e z -> tipo blender) 
    - utiliza de voxels -> pixel com volume
    - Dispositivos 3d: impressora

## Dispositivos Graficos
### CRT -> 
medida em pixel é uma unidade lógica e não fisica.
tamanho fisico depende do dispostivo de projeção, depende da unidade minima de projeção. 
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
