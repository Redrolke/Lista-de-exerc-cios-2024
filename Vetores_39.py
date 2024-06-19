def calcular_coeficientes_linha_anterior(linha_anterior):
    nova_linha = [1]

    for i in range(len(linha_anterior) - 1):
        novo_coeficiente = linha_anterior[i] + linha_anterior[i + 1]
        nova_linha.append(novo_coeficiente)
    nova_linha.append(1)

    return nova_linha

def triangulo_de_pascal(n):
    if n <= 0:
        print("O número n precisa ser um inteiro positivo.")
        return

    triangulo = []
    linha_atual = [1]
    triangulo.append(linha_atual)
    for _ in range(1, n):
        proxima_linha = calcular_coeficientes_linha_anterior(linha_atual)
        triangulo.append(proxima_linha)
        linha_atual = proxima_linha
    return triangulo
def imprimir_triangulo(triangulo):
    for linha in triangulo:
        print(" ".join(map(str, linha)))

def main():

    n = int(input("Digite um número inteiro positivo n: "))
    triangulo = triangulo_de_pascal(n)
    imprimir_triangulo(triangulo)

if __name__ == "__main__":
    main()