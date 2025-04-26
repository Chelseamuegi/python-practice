# This function checks if a number is even or odd

def even_or_odd(num):
    # If number is divisible by 2, it is even
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(5)) #Expected output should be Odd
print(even_or_odd(8)) #Expected output should be Even