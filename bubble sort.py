#Creating bubble sort function
def bubble_sort(list1):
    for i in range(len(list1)):
        for j in range(0, (len(list1)-1)):
            if list1[j] > list1[j+1]:
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
    return list1


lists = [5, 3, 2, 8, 6, 7]
print(bubble_sort(lists))