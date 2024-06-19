def calcular_pontuacao(alunos, gabarito):
  resultados = []
  for aluno in alunos:
      pontuacao = 0
      for i in range(len(gabarito)):
          if aluno[i] == gabarito[i]:
              pontuacao += 1
      resultados.append(pontuacao)
  return resultados
matriz_respostas = [
  ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b'],
  ['b', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b'],
  ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b'],
  ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b'],
  ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b']
]
gabarito = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b']
resultados = calcular_pontuacao(matriz_respostas, gabarito)
for i, resultado in enumerate(resultados):
  print(f"Aluno {i+1}: Pontuação {resultado}")