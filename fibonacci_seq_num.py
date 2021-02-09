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
        first = 1
        second = 1
        fibo_list = [1]
        for i in range(n-1):
            temp = first
            first = second
            second = second + temp
            fibo_list.append(first)
        print(*fibo_list, sep=" ")
    return first

print(fibo_loop(12))

def fibo_pythonnic(n):
    first, second = 1,1
    for i in range(n-1):
        first, second = second, second + first
    return first
        
def fibo_rabbit(months, offsprings):

    parent, child = 1,1

    for i in range(months - 1):
        child,parent = parent, parent + (child*offsprings)
    print(child)
    return child


fibo_rabbit(5,3)

