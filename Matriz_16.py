def calcular_nota(respostas_aluno, gabarito):
    nota = 0
    for i in range(len(gabarito)):
        if respostas_aluno[i] == gabarito[i]:
            nota += 1
    return nota
def percentual_aprovacao(notas, media_aprovacao):
    count_aprovados = sum(1 for nota in notas if nota >= media_aprovacao)
    percentual = (count_aprovados / len(notas)) * 100
    return percentual
gabarito = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']
alunos = [
    {"matricula": 1, "respostas": ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']},
    {"matricula": 2, "respostas": ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']},
    {"matricula": 3, "respostas": ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']}
]
for aluno in alunos:
    matricula = aluno["matricula"]
    respostas_aluno = aluno["respostas"]
    nota_aluno = calcular_nota(respostas_aluno, gabarito)
    aluno["nota"] = nota_aluno
notas = [aluno["nota"] for aluno in alunos]
percentual_aprovacao = percentual_aprovacao(notas, 7.0)
for aluno in alunos:
    print(f"Matrícula: {aluno['matricula']}")
    print(f"Respostas: {aluno['respostas']}")
    print(f"Nota: {aluno['nota']}")
    print()

print(f"Percentual de aprovação: {percentual_aprovacao}%")