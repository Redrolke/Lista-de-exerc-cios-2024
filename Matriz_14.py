import numpy as np

numeros = np.arange(100)
np.random.shuffle(numeros)
cartela = numeros[:25]
cartela = cartela.reshape(5, 5)
print("Cartela de Bingo:")
print(cartela)