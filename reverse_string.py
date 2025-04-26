# This function reverses a string without using [::-1] or built in reverse method

# Define a function that takes a string input
def reverse_string(s):
    # Initialize an empty string to store result
    reversed_s = ""
    #loop through each character in the string input
    for char in s:
        # Add each character to the beginning of the result
        reversed_s = char + reversed_s
    return reversed_s

print(reverse_string("Chelsea"))
