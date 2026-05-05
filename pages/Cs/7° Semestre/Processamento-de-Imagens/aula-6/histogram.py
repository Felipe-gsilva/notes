import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import matplotlib


def get_histogram(img2):
    hist = [0] * 256
    for i in range(img2.shape[0]):
        for j in range(img2.shape[1]):
            pixel_val = int(img2[i, j])
            hist[pixel_val] += 1
    return hist


def get_grayscale_image(img):
    b = img[:, :, 0].astype(np.float32)
    g = img[:, :, 1].astype(np.float32)
    r = img[:, :, 2].astype(np.float32)
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray.astype(np.uint8)


def main():
    try:
        matplotlib.use("gtk3agg")
        img = cv.imread("imagem.png", 1)
        if img is None:
            print("Erro: Imagem 'imagem.jpg' não encontrada.")
            return

        print("Original:", img.shape, img.size, img.dtype)
        img_rgb_for_display = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img2 = get_grayscale_image(img)
        hist = get_histogram(img2)
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
        ax1.imshow(img_rgb_for_display)
        ax1.set_title("Original")
        ax1.axis("off")
        ax2.imshow(img2, cmap="gray", vmin=0, vmax=255)
        ax2.set_title("Escala de Cinza")
        ax2.axis("off")
        ax3.plot(hist, color="black")
        ax3.set_title("Histograma")
        ax3.set_xlim([0, 256])
        plt.show()

    except KeyboardInterrupt:
        print("Programa interrompido pelo usuário.")


if __name__ == "__main__":
    main()
