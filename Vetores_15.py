def main():
    vetor = []

    for i in range(20):
        valor = int(input(f"Digite um numero {i+1}: "))
        vetor.append(valor)

    elementos_unicos = []
    for valor in vetor:
        if valor not in elementos_unicos:
            elementos_unicos.append(valor)
    print("\nElementos únicos no vetor:")
    for elemento in elementos_unicos:
        print(elemento)

if __name__ == "__main__":
    main()