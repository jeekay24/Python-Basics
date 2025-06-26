def fibonacci(n):
    t1 = 0
    t2 = 1
    fib_arr = []

    for i in range(n):
        fib_arr.append(t1)
        next_term = t1+t2
        t1 = t2
        t2 = next_term

    return fib_arr


n = int(input("Enter the number:"))
fib = fibonacci(n)

print(fib)
