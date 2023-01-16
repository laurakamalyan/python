list1 = [1, 2, 3, 4]

# out-of-place algorithm
def reverse1(arr):
    arr2 = []
    for i in range(len(arr) - 1, -1, -1):
        arr2.append(arr[i])

    for i in range(len(arr)):
        arr[i] = arr2[i]


# in-place algorithm
# auxiliary variables - i, j, temp
def reverse2(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1


# we can use only i and temp auxiliary variables
def reverse3(arr):
    for i in range(len(arr) // 2):
        temp = arr[i]
        arr[i] = arr[len(arr) - 1 - i]
        arr[len(arr) - 1 - i] = temp


reverse1(list1)
print(list1)
