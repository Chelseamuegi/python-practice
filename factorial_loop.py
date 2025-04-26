# This function computes a factorial using a loop

def factorial(n):
    result = 1
    for i in range(1,n - 1):
        result *= i
    return result


n = 5
result = factorial(n)
print(f"The factorial of {n} is {result} ")