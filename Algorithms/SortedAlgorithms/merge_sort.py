def split_list(arr):
    if len(arr) == 1: return arr
    else:
        mid_index = len(arr) // 2
        left_arr = arr[:mid_index]
        right_arr = arr[mid_index:]

        left = split_list(left_arr)
        right = split_list(right_arr)
        return merge_lists(left, right)


def merge_lists(left, right):
    arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        # compare the elements of two sorted sublists and merge them into one
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1

    # if there are elements left add them to the result
    if i < len(left): arr += left[i:]
    if j < len(right): arr += right[j:]

    return arr


list1 = [2, 5, 21, 4, 12, 6, 2]
result = split_list(list1)
print(result)
