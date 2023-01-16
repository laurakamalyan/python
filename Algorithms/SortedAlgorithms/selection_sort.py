def selection_sort_min(arr):
    for i in range(len(arr) - 1):
        min_element = arr[i]
        index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < min_element:
                min_element = arr[j]
                index = j

        arr[index] = arr[i]
        arr[i] = min_element
    print(arr)


def selection_sort_max(arr):
    for i in range(len(arr) - 1, -1, -1):
        index = i
        max_element = arr[i]

        for j in range(i):
            if arr[j] > max_element:
                max_element = arr[j]
                index = j

        arr[index] = arr[i]
        arr[i] = max_element

    print(arr)


alist = [5, 11, 5, 80, 5, 45, 7, 2, 33]
selection_sort_max(alist)
