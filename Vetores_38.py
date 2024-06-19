def main():

  vetor = []

  print("Digite 10 valores numéricos:")
  for i in range(10):
      valor = float(input(f"Digite o {i+1}º valor: "))
      insere_ordenado(vetor, valor)
  print("\nValores ordenados:")
  print(vetor)

def insere_ordenado(vetor, valor):
  posicao = 0
  while posicao < len(vetor) and valor > vetor[posicao]:
      posicao += 1
  vetor.insert(posicao, valor)

if __name__ == "__main__":
  main()