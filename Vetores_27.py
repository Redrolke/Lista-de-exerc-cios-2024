def is_prime(n):
  """Função para verificar se um número é primo."""
  if n <= 1:
      return False
  if n == 2:
      return True
  if n % 2 == 0:
      return False
  for i in range(3, int(n**0.5) + 1, 2):
      if n % i == 0:
          return False
  return True

def main():
  vetor = []
  print("Digite 10 números inteiros para o vetor:")
  for i in range(10):
      numero = int(input(f"Digite o número {i+1}: "))
      vetor.append(numero)
  print("\nNúmeros primos e suas respectivas posições no vetor:")
  for i in range(10):
      if is_prime(vetor[i]):
          print(f"Número primo: {vetor[i]} na posição {i}")

if __name__ == "__main__":
  main()