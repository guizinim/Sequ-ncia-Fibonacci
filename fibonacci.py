def pertence_fibonacci(numero):
  if numero < 0:
    return f"{numero} é um número negativo e não pertence à Sequência de Fibonacci."

  anterior = 0
  atual = 1

  while atual <= numero:
    if numero == atual:
      return f"{numero} pertence à Sequência de Fibonacci!"

    anterior, atual = atual, anterior + atual

  return f"{numero} não pertence à Sequência de Fibonacci."

numero = int(input("Informe um número: "))
resultado = pertence_fibonacci(numero)
print(resultado)
