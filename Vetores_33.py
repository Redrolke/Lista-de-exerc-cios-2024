def main():

  vetor = []
  print("Digite os 15 elementos do vetor:")
  for i in range(15):
      elemento = int(input(f"Digite o elemento {i+1}: "))
      vetor.append(elemento)

  i = 0
  while i < len(vetor):
      if vetor[i] == 0:
          for j in range(i, len(vetor) - 1):
              vetor[j] = vetor[j + 1]
          vetor[len(vetor) - 1] = 0
          i -= 1
      i += 1
  vetor_compactado = [elem for elem in vetor if elem != 0]
  print("\nVetor compactado:")
  print(vetor_compactado)

if __name__ == "__main__":
  main()