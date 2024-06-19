matriz_alunos = []
for i in range(5):
    matricula = int(input(f"Digite a matrícula do aluno {i+1}: "))
    media_provas = int(input(f"Digite a média das provas do aluno {i+1}: "))
    media_trabalhos = int(input(f"Digite a média dos trabalhos do aluno {i+1}: "))

    nota_final = media_provas + media_trabalhos

    matriz_alunos.append([matricula, media_provas, media_trabalhos, nota_final])


maior_nota_final = float('-inf')
matricula_maior_nota = None

for aluno in matriz_alunos:
    if aluno[3] > maior_nota_final:
        maior_nota_final = aluno[3]
        matricula_maior_nota = aluno[0]
notas_finais = [aluno[3] for aluno in matriz_alunos]
media_notas_finais = sum(notas_finais) / len(notas_finais)
print(f"Matrícula do aluno com maior nota final: {matricula_maior_nota}")
print(f"Média aritmética das notas finais: {media_notas_finais}")