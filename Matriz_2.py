def main():

    matriz = [[0] * 5 for _ in range(5)]
    for i in range(5):
        matriz[i][i] = 1
    print("Matriz 5x5 com diagonal principal de 1s:")
    for linha in matriz:
        print(linha)

if __name__ == "__main__":
    main()