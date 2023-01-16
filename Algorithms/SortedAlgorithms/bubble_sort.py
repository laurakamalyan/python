# algorithm with for circle
def bubble_sort_for_circle(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                item = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = item
    return arr


# algorithm with while circle
def bubble_sort_while_circle(arr):
    i = 0
    while i < len(arr) - 1:
        j = 0
        while j < len(arr) - 1 - i:
            if arr[j] > arr[j + 1]:
                item = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = item
            j += 1
        i += 1

    return arr


# algorithm without temporary variable
def bubble_sort(arr):
    for i in range(len(arr) - 1, -1, -1):
        for j in range(i):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


unsorted_list = [6, 12, 4, 3, 8, 18, 2, 9, 11]

print(bubble_sort_for_circle(unsorted_list))
print(bubble_sort_while_circle(unsorted_list))
print(bubble_sort(unsorted_list))
