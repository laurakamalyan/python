def quick_sort(arr):
    if len(arr) <= 1: return arr

    support_element = arr[0]
    min_elements = []
    max_elements = []
    center_elements = []

    for i in range(len(arr)):
        if arr[i] < support_element:
            min_elements.append(arr[i])
        elif arr[i] > support_element:
            max_elements.append(arr[i])
        else:
            center_elements.append(arr[i])

    min_elements = quick_sort(min_elements)
    max_elements = quick_sort(max_elements)
    result = min_elements + center_elements + max_elements
    return result


llist = [1, 8, 63, 21, 8]
print(quick_sort(llist))
