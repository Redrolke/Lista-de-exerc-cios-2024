def main():
  valores = []

  for i in range(5):
      valor = float(input(f"Digite o {i+1}º numero: "))
      valores.append(valor)
  maior = valores[0]
  menor = valores[0]
  soma = 0
  for valor in valores:
      if valor > maior:
          maior = valor
      if valor < menor:
          menor = valor
      soma += valor
  media = soma / 5
  print("\nnumeros digitados:", valores)
  print(f"Maior numero: {maior}")
  print(f"Menor numero: {menor}")
  print(f"Média dos numeros: {media}")

if __name__ == "__main__":
  main()