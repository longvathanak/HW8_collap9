def reverse_ascending(numbers):
    if len(numbers) <= 1:
        return numbers

    central = numbers[len(numbers) // 2]
    left = []
    middle = []
    right = []
    
    for x in numbers:
        if x > central:
            left.append(x)
        elif x == central:
            middle.append(x)
        else:
            right.append(x)

    return reverse_ascending(left) + middle + reverse_ascending(right)
    ...
print(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3]))

