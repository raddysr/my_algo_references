def fibo_func_recu(n):
   
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        return("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return fibo_def_rec(n-1) + fibo_def_rec(n-2)
 
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
