import numpy as np


def erro_maximo(matriz_1, matriz_2):
    if matriz_1.shape != matriz_2.shape:
        raise ValueError("As matrizes devem ter o mesmo formato.")
    erro = np.abs(matriz_1 - matriz_2)
    erro_max = np.max(erro)
    return erro_max


def erro_medio_absoluto(matriz_1, matriz_2):
    if matriz_1.shape != matriz_2.shape:
        raise ValueError("As matrizes devem ter o mesmo formato.")
    erro = np.abs(matriz_1 - matriz_2)
    erro_medio = np.mean(erro)
    return erro_medio


def erro_quadratico_medio(matriz_1, matriz_2):
    if matriz_1.shape != matriz_2.shape:
        raise ValueError("As matrizes devem ter o mesmo formato.")
    erro = (matriz_1 - matriz_2) ** 2
    erro_quadratico_medio = np.mean(erro)
    return erro_quadratico_medio


def coeficiente_jaccard(matriz_1, matriz_2):
    if matriz_1.shape != matriz_2.shape:
        raise ValueError("As matrizes devem ter o mesmo formato.")
    tolerancia = 5
    intersecao = np.sum(
        (matriz_1 > 0) & (matriz_2 > 0) & (np.abs(matriz_1 - matriz_2) <= tolerancia)
    )
    uniao = np.sum((matriz_1 > 0) | (matriz_2 > 0))

    if uniao == 0:
        return 1.0

    jaccard = intersecao / uniao
    return jaccard


def main():
    matriz_1 = np.array([[255, 255, 255], [255, 0, 255], [255, 255, 255]])
    matriz_2 = np.array([[250, 250, 250], [250, 1, 250], [250, 250, 250]])

    print("Matriz Original:")
    print(erro_maximo(matriz_1, matriz_2))
    print("Matriz Processada:")
    print(erro_medio_absoluto(matriz_1, matriz_2))
    print("Erro Quadrático Médio:")
    print(erro_quadratico_medio(matriz_1, matriz_2))
    print("Raiz do Erro Quadrático Médio:")
    print(np.sqrt(erro_quadratico_medio(matriz_1, matriz_2)))
    print("Coeficiente de Jaccard:")
    print(coeficiente_jaccard(matriz_1, matriz_2))


if __name__ == "__main__":
    main()
