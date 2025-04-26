# This function computes a factorial using a loop

def factorial(n):
    result = 1
    #loop from 1 to n
    for i in range(1,n - 1):
        #Multiply results by each number
        result *= i
    return result


n = 7
result = factorial(n)
print(f"The factorial of {n} is {result} ")