def replace_last(numbers):
      if not numbers:
        return numbers
      else:
        last_element = numbers[-1]
        numbers.remove(last_element)
        numbers.insert(0, last_element)
        return numbers
      
# test case
numbers = [5, 9, 4, 8,3,7]
print(replace_last(numbers))

numbers = [2,3,4,7,5,1]
print(replace_last(numbers))

numbers = [10,9,6,8,3,5,7]
print(replace_last(numbers))
