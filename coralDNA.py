def ncheck(n):
    if n < 0:
        return "The number must be positive."


def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num


def fib(n):
    fib_1, fib_2 = 0, 1
    for tmp_fib in range(n):
        tmp_fib = fib_1
        fib_1 = fib_1 + fib_2
        fib_2 = tmp_fib
        print(fib_1)

ncheck(n)
factorial(6)
fib(6)