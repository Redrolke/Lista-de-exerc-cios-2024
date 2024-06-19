def main():

    a = int(input("Digite o primeiro número : "))
    b = int(input("Digite o segundo número : "))
    vetor_a = num_para_vetor(a)
    vetor_b = num_para_vetor(b)
    tamanho_maximo = max(len(vetor_a), len(vetor_b))
    vetor_soma = [0] * (tamanho_maximo + 1)
    carry = 0

    for i in range(tamanho_maximo):
        digito_a = vetor_a[i] if i < len(vetor_a) else 0
        digito_b = vetor_b[i] if i < len(vetor_b) else 0
        soma = digito_a + digito_b + carry

        if soma >= 10:
            vetor_soma[i] = soma - 10
            carry = 1
        else:
            vetor_soma[i] = soma
            carry = 0

    if carry > 0:
        vetor_soma[tamanho_maximo] = carry

    print("\nVetor de dígitos de a:", vetor_a)
    print("Vetor de dígitos de b:", vetor_b)
    print("Vetor resultante da soma:", vetor_soma[::-1])
def num_para_vetor(numero):
    """ Converte um número em um vetor de dígitos """
    vetor = []
    while numero > 0:
        vetor.append(numero % 10)
        numero //= 10
    return vetor

if __name__ == "__main__":
    main()