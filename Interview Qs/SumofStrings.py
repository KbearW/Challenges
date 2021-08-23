def sumOfStrings(a,b):
    sum = ''
    digits = [0] * max(len(a), len(b))
    # print(digits)

    # Didn't ask for inplace, okay to use [::-1] function here
    a = a[::-1]
    b = b[::-1]

    # Can use a helper function for this
    for i in range(len(a)):
        print(i, a[i])
        digits[i] += int(a[i])
    print(digits)

    for j in range(len(b)):
        print(j, b[j])
        digits[j] += int(b[j])
    print(digits)

    # can be optiumized w .reduce() or .map() or lambda combination... look into it
    for digit in digits:
        sum = str(digit) + sum

    print(sum)

sumOfStrings('119','9')