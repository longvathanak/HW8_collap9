def replace_last(numbers):
      if not numbers:
        return numbers
      else:
        last_element = numbers[-1]
        numbers.remove(last_element)
        numbers.insert(0, last_element)
        return numbers
      
# test case
numbers = [2, 3, 4, 1]
print(replace_last(numbers))

numbers = [1, 2, 3, 4]
print(replace_last(numbers))

numbers = [1]
print(replace_last(numbers))

numbers = []
print(replace_last(numbers))

