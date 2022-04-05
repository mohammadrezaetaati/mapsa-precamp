



def fib(i):
    if i<=0:
        return i
    
    else:
        print(fib(i-1)+fib(i-2))
        return (fib(i-1)+fib(i-2))
print(fib(10))