def ordena_vetor(A):

  if len(A) != 11:
      raise ValueError("O vetor deve conter exatamente 11 elementos.")
  parte1 = sorted(A[:6])
  parte2 = sorted(A[6:], reverse=True)
  A_ordenado = parte1 + parte2

  return A_ordenado

def main():

  A = [1, 2, 3, 4, 5, 6, 15, 14, 13, 12, 11]
  A_ordenado = ordena_vetor(A)
  print("Vetor ordenado:", A_ordenado)

if __name__ == "__main__":
  main()