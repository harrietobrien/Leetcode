def lexicoPermute(s):
    a = sorted(s)
    n = len(a) - 1
    while True:
        yield ''.join(a)
        # find the largest index j such that a[j] < a[j + 1]
        for j in range(n - 1, -1, -1):
            if a[j] < a[j + 1]:
                break
        else:
            return
        # find the largest index k > j such that a[j] < a[k]
        v = a[j]
        for k in range(n, j, -1):
            if v < a[k]:
                break
        # swap the value of a[j] with that of a[k]
        a[j], a[k] = a[k], a[j]
        # reverse the tail of the sequence
        a[j + 1:] = a[j + 1:][::-1]


print(list(lexicoPermute('data')))
