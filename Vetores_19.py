def main():
    vetor = []

    for i in range(50):
        valor = (i + 5 * i) % (i + 1)
        vetor.append(valor)
    print("Vetor preenchido:")
    print(vetor)

if __name__ == "__main__":
    main()