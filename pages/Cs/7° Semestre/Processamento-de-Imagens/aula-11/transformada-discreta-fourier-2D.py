# Transformada discreta de fourier (2D)
from math import pi
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from tqdm import tqdm


def fourier_transform_2d(img: np.ndarray):
    pbar = tqdm(total=img.shape[0] * img.shape[1], desc="Calculating DFT")
    M, N, _ = img.shape
    out = np.zeros(img.shape, dtype=complex)
    for m in range(M):
        for n in range(N):
            pbar.update(1)
            for u in range(M):
                for v in range(N):
                    out[m, n] += img[u, v] * np.exp(2j * pi * ((u*m) / M + (v * n) / N ))

    pbar.close()
    return out


def inverted_fourier_transform_2d(img: np.ndarray):
    pbar = tqdm(total=img.shape[0] * img.shape[1], desc="Calculating inverse DFT")
    M, N, _ = img.shape
    out = np.zeros(img.shape, dtype=complex)
    for m in range(M):
        for n in range(N):
            pbar.update(1)
            for u in range(M):
                for v in range(N):
                    out[m, n] += img[u, v] * np.exp(-2j * pi * ((u*m) / M + (v * n) / N ))

    pbar.close()
    return (1 / (M * N)) * out


def get_grayscale_image(img: np.ndarray) -> np.ndarray:
    r = img[:, :, 0].astype(np.float32)
    g = img[:, :, 1].astype(np.float32)
    b = img[:, :, 2].astype(np.float32)
    # Fórmula de luminosidade padrão
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray.astype(np.uint8)


img_in = Image.open("aula-6/imagem.jpg").convert(("RGB"))
img_in = np.asarray(img_in)
image_gray = get_grayscale_image(img_in)
img_out = abs(fourier_transform_2d(img_in))


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 12))
ax1.imshow(img_in)
ax2.imshow(img_out, cmap="gray")
plt.show()
plt.show()
