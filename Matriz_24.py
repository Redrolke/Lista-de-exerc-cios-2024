import numpy as np
import random

def proxima_jogada(tabuleiro):

    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                tabuleiro[i][j] = -1
                if verifica_vitoria(tabuleiro, -1):
                    return i, j  
                tabuleiro[i][j] = 0

    posicoes_vazias = [(i, j) for i in range(3) for j in range(3) if tabuleiro[i][j] == 0]
    return random.choice(posicoes_vazias)
def verifica_vitoria(tabuleiro, jogador):

    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)):
            return True
        if all(tabuleiro[j][i] == jogador for j in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True
    if all(tabuleiro[i][2-i] == jogador for i in range(3)):
        return True

    return False

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(' '.join(map(str, linha)))

def main():

    tabuleiro = np.array([
        [-1, 1, 1],
        [-1, -1, 0],
        [0, 1, 0]
    ])

    print("Tabuleiro atual:")
    imprimir_tabuleiro(tabuleiro)
    proxima_jogada_i, proxima_jogada_j = proxima_jogada(tabuleiro)
    tabuleiro[proxima_jogada_i][proxima_jogada_j] = -1

    print("\nPróxima jogada (minha peça -1):")
    imprimir_tabuleiro(tabuleiro)

if __name__ == "__main__":
    main()