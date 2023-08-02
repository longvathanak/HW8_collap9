def chunking_by(numbers, chunck):
    ...
    n = len(numbers)
    new_list=[]
    for i in range(0,n,chunck):
        x = numbers [i:chunck+i]
        new_list.append(x)

    return new_list


print(chunking_by([5, 4, 7, 3, 4, 5, 4], 3))
print(chunking_by([3, 4, 5], 1))


