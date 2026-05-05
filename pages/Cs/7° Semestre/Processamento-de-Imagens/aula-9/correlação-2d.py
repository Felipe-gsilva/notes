import numpy as np

image = np.array(
    [
        [3, 1, 0, 5, 18, 6, 3, 27, 36],
        [90, 255, 0, 0, 251, 3, 18, 4, 7],
        [10, 20, 30, 40, 50, 60, 70, 80, 90],
        [9, 100, 9, 110, 6, 120, 6, 130, 18],
        [145, 190, 1, 2, 3, 4, 5, 6, 7],
        [90, 8, 49, 9, 36, 10, 27, 11, 18],
        [12, 13, 14, 15, 16, 17, 18, 19, 20],
        [255, 14, 255, 0, 0, 0, 0, 6, 9],
        [18, 27, 36, 45, 90, 180, 0, 255, 10],
    ]
)


def get_k_neighborhood(
    image: np.ndarray, i: int, j: int, kernel_w: int, kernel_h: int
) -> np.ndarray:
    neighborhood = image[i : i + kernel_w, j : j + kernel_h]
    return neighborhood


def correlation_2D(image: np.ndarray, kernel) -> np.ndarray:
    w, h = image.shape
    kernel_w, kernel_h = 3, 3
    output_w = w - kernel_w + 1
    output_h = h - kernel_h + 1
    output = np.zeros((output_w, output_h), dtype=np.uint8)

    for i in range(output_w):
        for j in range(output_h):
            neighborhood = get_k_neighborhood(image, i, j, kernel_w, kernel_h)
            output[i, j] = int(np.sum(neighborhood * kernel))

    return output


# reading user input for convolution or correlation
o = input("Enter 'c' for convolution or 'r' for correlation: ")
kernel = np.array([[1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9]])
if o == "c":
    kernel = np.flip(kernel)

output = correlation_2D(image, kernel)

# pretty print this matrix
print(output)
