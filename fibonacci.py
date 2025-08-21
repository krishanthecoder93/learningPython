def fibonacci(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        fib_sequence=[0,1]
        fib_sequence.extend(map(lambda i:fib_sequence[i-1]+fib_sequence[i-2],range(2,n)))
        return fib_sequence
fibonacci_sequence= fibonacci(10)
print(fibonacci_sequence)