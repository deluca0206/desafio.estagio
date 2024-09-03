def fibonacci_check(n):
    a, b = 0, 1

    if n == 0:
        return f"O número {n} pertence à sequência de Fibonacci."
    while b <= n:
        if b == n:
            return f"O número {n} pertence a sequência de Fibonacci."
        a, b = b, a + b

    return f"O número {n} não pertence a sequência de Fibonacci."

numero = int(input("Informe um número: "))
resultado = fibonacci_check(numero)
print(resultado)