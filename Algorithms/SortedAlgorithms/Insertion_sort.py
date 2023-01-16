def insertion_sort(arr):
    length = len(arr)
    for i in range(1, length):
        j = i
        while j != 0 and arr[j] < arr[j - 1]:
            item = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = item
            #arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

    return arr


def insertion_sort2(arr):
    for i in range(1, len(arr)):
        item = arr[i]
        j = i - 1
        while j >= 0 and item < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = item

    return arr


unsorted_list = [5, 20, 3, 8, 21, 4, 0]
sorted_list = insertion_sort2(unsorted_list)
print(sorted_list)
