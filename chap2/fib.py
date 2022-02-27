def fib(n: int) -> int:
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fib(n-1) + fib(n-2)


number = int(input("enter fib number: "))
result = fib(number)
print(result)
