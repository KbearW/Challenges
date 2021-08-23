def sumOfStrings(a,b):
    sum = ''
    digits = [0] * max(len(a), len(b))
    print(digits)

    a = a[::-1]
    b = b[::-1]

    for i in range(len(a)):
        print(i, a[i])
        digits[i] += int(a[i])
    print(digits)

    for j in range(len(b)):
        print(j, b[j])
        digits[j] += int(b[j])
    print(digits)

    for digit in digits:
        sum = str(digit) + sum

    print(sum)

sumOfStrings('119','9')