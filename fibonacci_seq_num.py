
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
print(fibo_def_rec(10))
 
def fibo_func_loop(n):
    a = 0
    b = 1
     
    # Check is n is less
    # than 0
    if n < 0:
        print("Incorrect input")
         
    # Check is n is equal
    # to 0
    elif n == 0:
        return 0
       
    # Check if n is equal to 1
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b

print(fibo_func_recu(10))
