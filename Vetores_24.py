def main():

    alunos = []
    alturas = []
    print("Digite os dados dos 10 alunos (número do aluno e altura em metros):")
    for i in range(10):
        numero_aluno = int(input(f"Digite o número do aluno {i+1}: "))
        altura_aluno = float(input(f"Digite a altura do aluno {i+1} (em metros): "))
        alunos.append(numero_aluno)
        alturas.append(altura_aluno)
    indice_mais_baixo = alturas.index(min(alturas))
    indice_mais_alto = alturas.index(max(alturas))
    numero_mais_baixo = alunos[indice_mais_baixo]
    altura_mais_baixo = alturas[indice_mais_baixo]
    numero_mais_alto = alunos[indice_mais_alto]
    altura_mais_alto = alturas[indice_mais_alto]
    print(f"\nAluno mais baixo é o Número {numero_mais_baixo}, Altura {altura_mais_baixo:.2f} metros")
    print(f"Aluno mais alto é o Número {numero_mais_alto}, Altura {altura_mais_alto:.2f} metros")

if __name__ == "__main__":
    main()