def binary_search(array, key, min_index, max_index):

    mid = int((min_index+max_index)/2)
    if key == array[mid]:
        return f'{key} is at index {mid+1}'
    elif key < array[mid]:
        return binary_search(array, key, min_index, mid - 1)
    elif key > array[mid]:
        return binary_search(array, key, mid + 1, max_index)


nums = [2, 3, 5, 7, 9]
key = 9
min_index = 0
max_index = len(nums) - 1
x = binary_search(nums, key, min_index, max_index)
print(x)


def binary_searching(array, key):
    min_indexx = 0
    max_indexx = len(array) - 1
    if key < array[min_indexx] or key > array[max_indexx]:
        return "key not found"
    for i in range(len(array)):
        mid = int((min_indexx + max_indexx)/2)
        if key == array[mid]:
            return f"{key} is located at index {mid+1}"

        elif key > array[mid]:
            min_indexx = mid + 1

        elif key < array[mid]:
            max_indexx = mid - 1


A = [1, 2, 4, 5, 7, 8, 9]
key = 9
a = binary_searching(A, key)
print(a)


