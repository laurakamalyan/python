def counting_sort(arr, length):
    # fill array with zeros
    count = [0] * length

    # count of each element in arr
    for i in range(len(arr)):
        count[arr[i]] = count[arr[i]] + 1

    # array sorting
    j = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[j] = i
            j += 1
            count[i] -= 1

    print(arr)


alist = [2, 5, 0, 1, 4, 1, 1, 6]
max_element = max(alist)
counting_sort(alist, max_element + 1)
