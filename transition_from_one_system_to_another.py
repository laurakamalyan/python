def ten_to_two(num):
    remain = ""

    while num != 0:
        m = int(num % 2)
        remain += str(m)
        num = (num - m) / 2

    result = ""
    for i in range(len(remain) - 1, -1, -1):
        result += remain[i]

    return result


def two_to_ten(num):
    result = 0
    j = len(num) - 1

    for i in range(len(num)):
        result += int(num[i]) * (2 ** j)
        j -= 1

    return result


def two_to_eight(num):
    result = ""
    n = ""
    if len(num) % 3 == 1:
        num = "00" + num
    elif len(num) % 3 == 2:
        num = "0" + num

    for i in range(len(num)):
        if len(n) == 3:
            result += str(two_to_ten(n))
            n = ""
        n += num[i]
    result += str(two_to_ten(n))
    return result


def eight_to_two(num):
    result = ""
    n = str(num)
    for i in range(len(n)):
        result += ten_to_two(int(n[i]))

    return result


def two_to_sixteen(num):
    a = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}

    if len(num) % 4 == 1:
        num = "000" + num
    elif len(num) % 4 == 2:
        num = "00" + num
    elif len(num) % 4 == 3:
        num = "0" + num

    result = ""
    n = ""

    for i in range(len(num)):
        if len(n) == 4:
            r = two_to_ten(n)
            if r > 9:
                r = a.get(str(r))
            result += str(r)
            n = ""
        n += num[i]

    r = two_to_ten(n)
    if r > 9:
        r = a.get(str(r))
    result += str(r)

    return result


def sixteen_to_two(num):
    a = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}
    result = ""

    for i in range(len(num)):
        b = False
        for key, value in a.items():
            if num[i] == value:
                result += ten_to_two(int(key))
                b = True
        if b is False:
            result += ten_to_two(int(num[i]))

    return result


n1 = 44
n2 = "101100"
n3 = 54
n4 = "2C"
print(f"{n1}\u2081\u2080 -> {ten_to_two(n1)}\u2082")
print(f"{n2}\u2082 -> {two_to_ten(n2)}\u2081\u2080")
print(f"\n{n2}\u2082 -> {two_to_eight(n2)}\u2088")
print(f"{n3}\u2088 -> {eight_to_two(n3)}\u2082")
print(f"\n{n2}\u2082 -> {two_to_sixteen(n2)}\u2081\u2086")
print(f"{n4}\u2081\u2086 -> {sixteen_to_two(n4)}\u2082")
