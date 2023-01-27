def Linear_search(array, key, i):
    if array[i] == key:
        return f'{key} is at index {i+1}'
    if len(array) == i+1 and array[i] != key:
        return f'Element not found'
    else:
        return Linear_search(array, key, i+1)


nums = [2, 3, 5, 7, 9]
key = 5
i = 0
x = Linear_search(nums, key, i)
print(x)