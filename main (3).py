def count_valid_numbers(p):
    if p == 1:
        return 2
    a = [0] * (p + 1)
    b = [0] * (p + 1)
    
    a[1] = 2
    b[1] = 0

    for i in range(2, p + 1):
        a[i] = a[i - 1] + b[i - 1]
        b[i] = a[i - 1]

    return a[p] + b[p]


p = int(input("Введіть p: "))
print(count_valid_numbers(p))
