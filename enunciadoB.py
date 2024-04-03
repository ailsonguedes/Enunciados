import math

def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s*s == x

def is_fibonacci(n):
    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

numero = int(input("Informe um número: "))
if is_fibonacci(numero):
    print(f"Sim, {numero} pertence à sequência de Fibonacci.")
else:
    print(f"Não, {numero} não pertence à sequência de Fibonacci.")
