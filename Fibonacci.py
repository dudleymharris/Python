# Python 3: Fibonacci
import pandas as pd
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
c = input("Fibonacci < ")
fib(float(c))
