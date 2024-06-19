def main():

    matriz = []
    for i in range(4):
        linha = []
        for j in range(4):
            valor = float(input(f"Digite o valor para a posição [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)
    contador = 0
    for linha in matriz:
        for valor in linha:
            if valor > 10:
                contador += 1

    print(f"A matriz possui {contador} valores maiores que 10.")

if __name__ == "__main__":
    main()