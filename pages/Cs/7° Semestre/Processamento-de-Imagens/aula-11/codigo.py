from numpy import fft
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]

X = fft.fft(x)

magnitude = abs(X)

freqs = np.arange(len(x)) / len(x)

plt.stem(freqs, magnitude)
plt.xlabel('Frequência Normalizada')
plt.ylabel('Magnitude')
plt.title('Magnitude do Espectro de Frequências')
plt.grid()
plt.show()
