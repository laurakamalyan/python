def counting_sort(arr, length):
    # fill array with zeros
    count = [0] * length

    # count of each element in arr
    for i in range(len(arr)):
        count[arr[i]] = count[arr[i]] + 1

    # calculate cumulative sum
    for i in range(1, length):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = len(arr) - 1
    output = [0] * len(arr)
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    # copy the sorted elements into original array
    for i in range(0, len(arr)):
        arr[i] = output[i]


alist = [2, 5, 0, 1, 4, 1, 1, 6]
max_element = max(alist)
counting_sort(alist, max_element + 1)
print(alist)



