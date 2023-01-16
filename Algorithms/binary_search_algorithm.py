# iterative method
def binary_search_algorithm1(arr):
    search_item = 24

    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2

    while low <= high:
        if arr[mid] == search_item:
            return f"Index of search element: {mid}"
        elif arr[mid] < search_item:
            low = mid + 1
        else:
            high = mid - 1

        mid = (low + high) // 2

    return "Element not found"


# recursive method
def binary_search_algorithm2(arr, low, high):
    search_element = 41
    mid = (low + high) // 2

    if low <= high:

        if arr[mid] == search_element:
            return f"Index of search element: {mid}"
        elif arr[mid] < search_element:
            low = mid + 1
        else:
            high = mid - 1

        return binary_search_algorithm2(arr, low, high)

    else: return "Element not found."


array = [24, 12, 54, 50, 41, 39, 45, 32]
sorted_arr = sorted(array) # [12, 24, 32, 39, 41, 45, 50, 54]

low_index = 0
high_index = len(sorted_arr) - 1

print(binary_search_algorithm1(sorted_arr))
print(binary_search_algorithm2(sorted_arr, low_index, high_index))
