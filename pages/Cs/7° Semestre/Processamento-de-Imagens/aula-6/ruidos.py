import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import matplotlib


def apply_gaussian_noise(image, mean=0, stddev=1):
    noise = np.random.normal(mean, stddev, image.shape)

    noise_img = image + noise

    min_val = np.min(noise_img)
    max_val = np.max(noise_img)

    norm_img = 255 * (noise_img - min_val) / (max_val - min_val)
    return norm_img


def equalize_hist(img, b=255):
    new_img = img
    min = np.min(img)
    max = np.max(img)

    c = 255 / (max - min)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            new_img[i][j] = (c * img[i][j]) + b

    return new_img


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
        img2 = get_grayscale_image(img)
        hist = get_histogram(img2)
        fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(1, 5, figsize=(10, 5))
        ax1.imshow(img2, cmap="gray", vmin=0, vmax=255)
        ax1.axis("off")
        img3 = apply_gaussian_noise(img2)
        ax2.imshow(img3, cmap="gray", vmin=0, vmax=255)
        ax1.set_title("Escala de Cinza")
        ax2.set_title("")
        ax2.axis("off")
        ax3.plot(hist, color="black")
        ax3.set_title("Histograma")
        ax3.set_xlim([0, 256])
        ax4.imshow(equalize_hist(img2), cmap="gray")
        ax5.plot(get_histogram(equalize_hist(img2)), color="black")
        plt.show()

    except KeyboardInterrupt:
        print("Programa interrompido pelo usuário.")


if __name__ == "__main__":
    main()
