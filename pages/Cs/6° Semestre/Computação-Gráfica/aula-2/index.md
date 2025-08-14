- GL_POINTS
- GL_LINES 
- GL_LINE_LOOP
- GL_LINE_STRIP

# Conceitos Iniciais 

Vetor: 
Direção:
Sentido de A para B:
Módulo ou intensiddade:

# Transformações geométricas
## Translacao (Translate)
Soma do vetor de Translacao T a P (ponto). 

## Escala (Scale)
Multiplicamos o vetor P (x, y, z) pela matriz 
$$
\begin{matrix}
s_x \ 0 \\
0 \ s_y \\
\end{matrix}
$$

## Cisalhamento (Shearing)>
Fator de deslocamento:

$$
\begin{matrix}
1 \ 0 \\
c_y \ 1 \\
\end{matrix}
$$


$$
\begin{matrix}
1 \ c_x \\
0 \ 1 \\
\end{matrix}
$$

## Espelhamento
Inverter (pelo eixo de )

Multiplicar pelo oposto do eixo que se quer refletir 

$$
\begin{bmatrix}
-1 & 0 \\
0 & -1 \\
\end{bmatrix}
$$

## Rotação

Matriz de rotação: 

$$
R(\tetha) \times P = 
\begin{bmatrix}
cos(\tetha) & -sin(\tetha) \\
sin(\tetha) & cos(\tetha) \\
\end{bmatrix}
$$

### Rotação no 3D
trave o eixo em si e use a formula acima :thumbsup:

# Transformocoes Homogeneas
## Coordenadas homogeneas
$$\begin{bmatrix} 1 & 0 & 0 & t_1 \\ 0 & 1 & 0 & t_2 \\ 0 & 0 & 1 & t_3 \\ 0 & 0 & 0 & t_4 \end{bmatrix}$$

Podemos fazer em Coordenadas Homogeneas todas as transformacoes como multiplicacoes em sequencia.

---
# opengl
glTranslatef
glScalef
glRotatef


