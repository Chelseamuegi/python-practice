#This is a function to find the sum of all digits in a number

#Define function that takes a positive integer
def sum_of_digits(n):
    # Initialize a variable to store the sum of digits
    total = 0
    #loop until the number becomes 0
    while n > 0:
        # Remove the last digit
        digit = n % 10
        total += digit
        n = n // 10

    return total

print(sum_of_digits(7851)) # Expected output should be 21
