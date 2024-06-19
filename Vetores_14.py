def main():
  vetor = []

  for i in range(10):
      valor = int(input(f"Digite um numero {i+1}: ")) 
      vetor.append(valor)
  valores_iguais = []

  for i in range(10):
      for j in range(i + 1, 10):
          if vetor[i] == vetor[j] and vetor[i] not in valores_iguais:
              valores_iguais.append(vetor[i])
  if valores_iguais:
      print("\nnumeros iguais encontrados no vetor:")
      for valor in valores_iguais:
          print(valor)
  else:
      print("\nNão foram encontrados numeros iguais no vetor.")

if __name__ == "__main__":
  main()