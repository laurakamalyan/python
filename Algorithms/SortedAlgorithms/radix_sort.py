def counting_sort(arr, place):
    length = 10 # 0, 1, ... , 9
    # fill array with zeros
    count = [0] * length

    # count of each digit in arr
    for i in range(len(arr)):
        x = arr[i] // place
        index = x % 10
        count[index] += 1

    # calculate prefix(cumulative) sum to find
    # the position of each index in the sorted output array
    j = 0
    for i in range(0, length):
        temp = count[i]
        count[i] = j
        j = j + temp

    print(count)

    # Build the output array
    output = [0] * len(arr)
    for i in range(len(arr)):
        index = (arr[i] // place) % 10
        new_index = count[index]
        output[new_index] = arr[i]
        count[index] += 1


    # copying the output array to arr[]
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radix_sort(arr):
    # get number of digits in maximum item
    max1 = max(arr)

    max_length = 0
    for n in str(max1):
        max_length += 1

    # Do counting sort for every digit
    place_value = 1
    for i in range(max_length):
        counting_sort(arr, place_value)
        place_value *= 10


list1 = [2, 20, 61, 187, 2, 619]
radix_sort(list1)
print(list1)
