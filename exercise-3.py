def remove_all_after(numbers, n):
    # check if the numbers is empty
    if not numbers: 
        return []
    
    # Iterate through the numbers to find the border element
    for index, element in enumerate(numbers):
        if element == n: 
            # return the numbers up to the indext where the border element is found
            return numbers[:index+1]
        
    #if the border element is not found return the original numbers 
    return numbers
   
#test case 
print(remove_all_after([1, 2, 3, 4, 5], 3))
print(remove_all_after([1, 1, 2, 2, 3, 3], 2))


