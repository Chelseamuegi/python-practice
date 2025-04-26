#This function adds all elements in a list and returns the sum
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
        return sum(numbers)

print(sum_list([23,45,12,33])) # expected output should be 113
