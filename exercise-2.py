def index_power(numbers, n):
# The code defines a function named 'index_power' that take two parameters: 'numbers' and 'n'.
    if n < 0 or n >= len(numbers): 
        return -1
# The function first checks if the value of 'n' is within the range of the 'numbers' list. 
# If it is not, the function return -1
    element = numbers[n]
    power = 1
    for i in range(1, n + 1):
        power *= element
    return power
# If the value of 'n' is within the range of the 'numbers' list, 
# the function selects the element at the 'n'th index and initializes a variable 'power' to 1.
# The function then iterates from 1 to 'n' and multiplies 'power' with the selected element. 
# This process is repeated until 'n' is reached.
# Finally, the function returns the value of 'power'


# test case
numbers = [1, 2, 3, 4]
n = 2
print(index_power(numbers, n))
numbers= [1, 2, 3]
n = 3
print(index_power(numbers, n))
numbers=[1, 3, 10, 100]
n=3
print(index_power(numbers, n))
numbers=[0, 1]
n=0
print(index_power(numbers, n))
array=[1, 2]
n=3
print(index_power(numbers, n))




