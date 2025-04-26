# This function reverses a string without using [::-1] or built in reverse method

def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

print(reverse_string("Chelsea"))
