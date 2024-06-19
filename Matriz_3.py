def main():

    matriz = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            matriz[i][j] = i * j
    print("Matriz preenchida com o produto da linha pelo número da coluna:")
    for linha in matriz:
        print(linha)

if __name__ == "__main__":
    main()