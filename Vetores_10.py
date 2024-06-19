notas = []
for i in range(15):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)

soma_notas = sum(notas)
media_geral = soma_notas / len(notas)
print(f"A média geral das notas dos {len(notas)} alunos é: {media_geral:.2f}")