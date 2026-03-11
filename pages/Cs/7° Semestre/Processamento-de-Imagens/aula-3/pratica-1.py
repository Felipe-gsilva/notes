import matplotlib.pyplot as plt
import matplotlib
import cv2 as cv
import numpy as np
from typing import List


def main():
    try:
        matplotlib.use("Qt5Agg")
        # Carregar a imagem
        img = cv.imread("imagem.jpg", 1)
        # Salvar a imagem em escala de cinza
        print(img.shape, img.size, img.dtype)

        img_r = img[:, :, 0].astype(np.float32)
        img_g = img[:, :, 1].astype(np.float32)
        img_b = img[:, :, 2].astype(np.float32)


        arr: List[np.float32] = []
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                arr.append((0.2989 * img_r[i][j] + 0.5870 * img_g[i][j] + 0.1140 * img_b[i][j]).astype(np.float32))

        img2 = np.array(arr).reshape(img.shape[0], img.shape[1])

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 12))
        ax1.imshow(img)
        ax2.imshow(img2, cmap='gray')
        plt.show()

    except KeyboardInterrupt:
        print("Programa interrompido pelo usuário.")


if __name__ == "__main__":
    main()
