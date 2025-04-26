# This function checks if a number is even or odd

def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(5)) #Expected output should be odd
print(even_or_odd(8)) #Expected output should be Even