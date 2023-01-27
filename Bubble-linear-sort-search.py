A = [64, 25, 12, 22, 11]
for i in range(len(A)):
    min_index = i
    for j in range(i + 1, len(A)):
        if A[min_index] > A[j]:
            min_index = j
    A[i], A[min_index] = A[min_index], A[i]

print("Selection Sort")
for i in range(len(A)):
    print("%d" % A[i], end=" ")

#Bubble Sort
B = [5, 1, 4, 2, 3]
for i in range(len(B) - 1):
    for j in range((len(B) - i) - 1):
        if B[j] > B[j+1]:
            temp = B[j]
            B[j] = B[j + 1]
            B[j + 1] = temp

print()
print("Bubble sort")
for i in range(len(B)):
    print("%d"% B[i], end=" ")

print()
#Linear search
C = [10, 50, 30, 70, 60, 20, 90]
print(C)
key = int(input("Enter Key"))


def linear_search(array):
    result = 0
    for element in range(len(array)):
        if array[element] == key:
            element += 1
            print("Key located at index:", element)
            result += 1
    if result == 0:
        print("Key not located in the array")




#Binary search
D = [2, 5, 6, 8, 10, 12, 24, 18, 22]
print(D)
keyb = int(input("Enter key for binary"))

def binary_search(array):
    result = 0
    min_index = 0
    max_index = (len(D) - 1)
    for i in range(len(D)):
        mid = int((min_index + max_index)/2)
        if keyb == D[mid]:
            mid += 1
            print("Your key is located at position:", mid)
            result += 1
            break
        if keyb > D[mid]:
            min_index = mid + 1
        if keyb < D[mid]:
            max_index = mid - 1

    if result == 0:
        print("Number not located in array")


binary_search(D)