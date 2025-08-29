Antialiasing 
- Amostragem de Área Ponderada.

Poligonos 
- Construção e preenchimento de polignos com formas arbitrárias.

--- 
# Rasterizacao: representacao matricial
Graficos sao dados por primitivas geometricas, passando algo vetorial (continuo) para matricial (discreto).

Dispositivos graficos: matrizes de pixels.

- algoritmos para segmentos de retas 
data uma reta qualquer com v1(x1, y2) e v2(x2, y2): 
1. Selecao de pixels imediatamente acima e abaixo (linhas densas)
2. Pixels obtidos pelo arredonamento dos valores de algum ponto do segmento (aproximacao)
3. Pixels obtidos por um pixel por coluna mais proximos da interseccao (mais bonito). (0 - 45 graus)
4. mesmo criterio para cada linha horizontal (paia) (45 - 90 graus)

Caracteristicas possiveis:
- Linearidade: parecer uma reta
- Precisao: pontos devem terminar e comecar nos vertices terminais.
- Densidade uniforme: pixels devem ser igualmente espacados.
- Intensidade independente da inclinacao: ou seja, se a inclinacao mudar, a reta deve parecer a mesma.
- Continuidade: Nao aprensetar interrupcao
- Rapidez.


# Aliasing
Primitiavas podem ter problemas, ou seja, serrilhar.

Filtro gaussiano (distribuicao normal) -> atribui um peso pro pixel central e pesos menores aos vizinhos (ou seja, borra os pixels)

# Preenchiento de poligono
checando vizinhos ou ate a fronteira, dado uma semente (posicao inicial)

para pintar pixel usa o ray casting (se esta ou nao no poligono).

Problema do vertice: vertices sao compartilhados entre arestas, logo o flip estara errado.
Se o vertice eh minimo para uma aresta e maximo para outra, inverta a paridade.
Se for minimo pras 2  arestas presentes, nao flipa, so pinta o pixel do vertice.
Se for maximo pras 2  arestas presentes, nao flipa e nem pinta.

Causa `sliver`, dentro do mesmo pixel ha outra aresta.


# Exercicios:
programa usando opengl para que o usuario informe
num de vertices para construir um poligono convexo, uma coord para cada vertice e sua cor de preenchimento.
