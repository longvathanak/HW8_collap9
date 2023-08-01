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
test_case_1 = [1, 2, 3, 4, 5]
test_case_2 = [5, 7, 10, 4, 2, 7, 8, 1, 3]

# Running the test cases
result_1 = reverse_ascending(test_case_1)
result_2 = reverse_ascending(test_case_2)

# Verifying the results
assert list(result_1) == [5, 4, 3, 2, 1]
assert list(result_2) == [10, 7, 5, 4, 8, 7, 2, 3, 1]

print("Test cases passed!")

