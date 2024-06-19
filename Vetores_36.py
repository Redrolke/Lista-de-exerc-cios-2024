def merge_sort(vetor):
    if len(vetor) <= 1:
        return vetor

    meio = len(vetor) // 2
    esquerda = merge_sort(vetor[:meio])
    direita = merge_sort(vetor[meio:])

    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado

def main():

    vetor = []
    print("Digite 10 números reais:")
    for i in range(10):
        numero = float(input(f"Digite o número {i+1}: "))
        vetor.append(numero)
    vetor_ordenado = merge_sort(vetor)
    print("\nElementos do vetor ordenado:")
    for num in vetor_ordenado:
        print(num, end=" ")

if __name__ == "__main__":
    main()