import numpy as np

def ler_matriz():
    matriz = []
    for i in range(2):
        linha = []
        for j in range(2):
            valor = float(input(f"Digite o valor da posição [{i+1}][{j+1}]: "))
            linha.append(valor)
        matriz.append(linha)
    return np.array(matriz)

def somar_matrizes(matriz1, matriz2):
    return matriz1 + matriz2
def subtrair_matrizes(matriz1, matriz2):
    return matriz2 - matriz1

def adicionar_constante(matriz, constante):
    matriz += constante
    return matriz
def imprimir_matrizes(matriz1, matriz2):
    print("Matriz 1:")
    print(matriz1)
    print("\nMatriz 2:")
    print(matriz2)
def main():
    print("Digite os elementos da Matriz 1:")
    matriz1 = ler_matriz()
    print("\nDigite os elementos da Matriz 2:")
    matriz2 = ler_matriz()

    while True:
        print("\nMenu de opções:")
        print("a) Somar as duas matrizes")
        print("b) Subtrair a primeira matriz da segunda")
        print("c) Adicionar uma constante às duas matrizes")
        print("d) Imprimir as matrizes")
        print("e) Sair do programa")

        opcao = input("\nDigite a opção desejada (a, b, c, d ou e): ").lower()

        if opcao == 'a':
            matriz_soma = somar_matrizes(matriz1, matriz2)
            print("\nMatriz resultante da soma:")
            print(matriz_soma)
        elif opcao == 'b':
            matriz_subtracao = subtrair_matrizes(matriz1, matriz2)
            print("\nMatriz resultante da subtração (Matriz2 - Matriz1):")
            print(matriz_subtracao)
        elif opcao == 'c':
            constante = float(input("\nDigite a constante que deseja adicionar às matrizes: "))
            matriz1 = adicionar_constante(matriz1, constante)
            matriz2 = adicionar_constante(matriz2, constante)
            print("\nMatrizes após adição da constante:")
            imprimir_matrizes(matriz1, matriz2)
        elif opcao == 'd':
            imprimir_matrizes(matriz1, matriz2)
        elif opcao == 'e':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Por favor, digite novamente.")
if __name__ == "__main__":
    main()