# with recursion

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
 
# with a loop

def fibo_loop(n):
    if n == 0:
        return 0 
    elif n == 1 or n == 2:
        return 1
    else:
        first = second = 1
        fibo_list = [1]
        for itr in range(n-1):
            temp = first
            first = second
            second = second + temp
            fibo_list.append(first)
        print(*fibo_list, sep=" ")
    return first

print(fibo_loop(12))
