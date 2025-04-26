#This function computes a factorial using  direct recursion

# Define a recursive function that takes a positive integer
def factorial_recursive(n):
    if n == 0:
        return 1

    return n * factorial_recursive(n - 1)

print(factorial_recursive(7)) #Expected output should be 5040
