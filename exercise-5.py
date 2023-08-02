def reverse_ascending(numbers):
    if len(numbers) <= 1:
        return numbers

    result = []
    sequence = [numbers[0]]

    for i in range(1, len(numbers)): 
        if numbers[i] > numbers[i-1]: 
            sequence.append(numbers[i])
        else: 
            result.extend(reversed(sequence))
            sequence = [numbers[i]]
    result.extend(reversed(sequence))
    return result
    ...
print(reverse_ascending([10, 7, 5, 4, 8, 7, 2, 3, 1]))

