# iterative method
# with for circle
def linear_search(arr):
    search_element = 8

    for i in range(len(alist)):
        if arr[i] == search_element:
            return i

    return "Element not found."


# with while circle
def linear_search2(arr, search = 77):
    i = 0
    while i != len(arr):
        if arr[i] == search: return i
        i += 1

    return "Element not found."


# recursive method
def linear_search3(arr, i):
    search = 6
    if i == len(arr): return "Element not found."

    if arr[i] == search: return  i
    else:
        i += 1
        return linear_search3(arr, i)


alist = [2, 6, 7, 8, 11, 5, 38]

print("Index of search element: ", linear_search(alist))
print("Index of search element: ", linear_search2(alist))

index = 0
print("Index of search element: ", linear_search3(alist, index))
