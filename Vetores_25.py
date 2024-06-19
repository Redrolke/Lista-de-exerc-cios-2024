def main():
    vetor = []
    numero = 0

    while len(vetor) < 100:
        if numero % 7 != 0 and str(numero)[-1] != '7':
            vetor.append(numero)
        numero += 1

    print("(Os primeiros 100 números naturais que não são múltiplos de 7 e não terminam com 7):")

    for i in range(0, 100, 10):
        print(vetor[i:i+10])

if __name__ == "__main__":
    main()
