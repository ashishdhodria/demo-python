def fact(n):
    if n == 1:
        return 2
    return n * fact(n - 1)


n = int(input("Enter a no."))
print(fact(n))