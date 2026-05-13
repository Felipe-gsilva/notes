import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def get_k_neighborhood(
    image: np.ndarray, i: int, j: int, kernel_w: int, kernel_h: int
) -> np.ndarray:
    neighborhood = image[i : i + kernel_w, j : j + kernel_h]
    return neighborhood


def get_grayscale_image(img: np.ndarray) -> np.ndarray:
    r = img[:, :, 0].astype(np.float32)
    g = img[:, :, 1].astype(np.float32)
    b = img[:, :, 2].astype(np.float32)
    # Fórmula de luminosidade padrão
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray.astype(np.uint8)


def convolution_2D(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    w, h = image.shape
    kernel_w, kernel_h = kernel.shape
    output_w = w - kernel_w + 1
    output_h = h - kernel_h + 1
    output = np.zeros((output_w, output_h))

    for i in range(output_w):
        for j in range(output_h):
            neighborhood = get_k_neighborhood(image, i, j, kernel_w, kernel_h)
            output[i, j] = np.sum(neighborhood * kernel)

    return output


# Kernel de Laplace (Vizinhança 8)
laplace_kernel_8 = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

# Kernel de Laplace (Vizinhança 4 - Anteriormente chamado de Canny)
laplace_kernel_4 = np.array([
    [0,  1,  0],
    [1, -4,  1],
    [0,  1,  0]
])

# Kernel de Sobel X (Detecta bordas verticais)
sobel_x_kernel = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

image_path = "../aula-6/imagem.jpg"

try:
    img_pil = Image.open(image_path).convert("RGB")
    image = np.asarray(img_pil)
    image_gray = get_grayscale_image(image)

    output_laplace_8 = convolution_2D(image_gray, laplace_kernel_8)
    output_laplace_8 = np.abs(output_laplace_8)

    output_laplace_4 = convolution_2D(image_gray, laplace_kernel_4)
    output_laplace_4 = np.abs(output_laplace_4)

    output_sobel_x = convolution_2D(image_gray, sobel_x_kernel)
    output_sobel_x = np.abs(output_sobel_x)

    # Exibe as imagens
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.title("Laplace (Viz 8)")
    plt.imshow(output_laplace_8, cmap="gray")
    plt.axis("off")
    plt.subplot(1, 3, 2)
    plt.title("Laplace (Viz 4)")
    plt.imshow(output_laplace_4, cmap="gray")
    plt.axis("off")
    plt.subplot(1, 3, 3)
    plt.title("Sobel (Eixo X)")
    plt.imshow(output_sobel_x, cmap="gray")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print(f"Erro: Não foi possível encontrar a imagem no caminho '{image_path}'.")
