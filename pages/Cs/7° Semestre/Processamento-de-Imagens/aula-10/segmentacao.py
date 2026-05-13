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


# Kernel de detecção de reta (Detecta bordas verticais)
x_kernel = np.array([
    [-1, 2, -1],
    [-1, 2, -1],
    [-1, 2, -1]
])

# Kernel de detecção de reta ( Detecta bordas horizontais)
y_kernel = np.array([
    [-1, -1, -1],
    [2, 2, 2],
    [-1, -1, -1]
])

kernel_45 = np.array([
    [-1, -1, 2],
    [-1, 2, -1],
    [2, -1, -1]
])

kernel_123 = np.array([
    [2, -1, -1],
    [-1, 2, -1],
    [-1, -1, 2]
])

image_path = "../aula-6/imagem.png"

try:
    img_pil = Image.open(image_path).convert("RGB")
    image = np.asarray(img_pil)
    # normalizar a imagem para o intervalo [0, 255]
    image = ((image - image.min()) / (image.max() - image.min()) * 255).astype(np.uint8)
    image_gray = get_grayscale_image(image)

    output_x = Image.fromarray(convolution_2D(image_gray, x_kernel))
    output_y = Image.fromarray(convolution_2D(image_gray, y_kernel))
    output_45 = Image.fromarray(convolution_2D(image_gray, kernel_45))
    output_123 = Image.fromarray(convolution_2D(image_gray, kernel_123))

    # Exibe as imagens
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 2, 1)
    plt.title("Detecção de Reta (Vertical)")
    plt.imshow(image_gray, cmap="gray")
    plt.axis("off")
    plt.subplot(2, 2, 2)
    plt.title("Detecção de Reta (Horizontal)")
    plt.imshow(output_y, cmap="gray")
    plt.axis("off")
    plt.subplot(2, 2, 3)
    plt.title("Detecção de Reta (45°)")
    plt.imshow(output_45, cmap="gray")
    plt.axis("off")
    plt.subplot(2, 2, 4)
    plt.title("Detecção de Reta (135°)")
    plt.imshow(output_123, cmap="gray")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print(f"Erro: Não foi possível encontrar a imagem no caminho '{image_path}'.")
