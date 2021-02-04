
def fibo_rec(n):
    if n < 0:
        return"Input must be bigger than a zero!!!"
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)
    
# Driver Program
print(fibo_rec(10))
 

def fibonacci_loop(n):
    if n == 0:
        return 0 
    elif n == 1 or n == 2:
        return 1
    else:
        new = old = 1
        
        fib_list = [1]
        for itr in range(n-1):
            temp = new
            new = old
            old = old + temp
            fib_list.append(new)
        print(*fib_list, sep=" ")
    return new

print(fibonacci_loop(12))
