def count_sequences(n):
    MOD = 12345
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    c = [0] * (n + 1)

    a[1], b[1], c[1] = 1, 1, 0

    for i in range(2, n + 1):
        a[i] = (a[i - 1] + b[i - 1] + c[i - 1]) % MOD
        b[i] = a[i - 1] % MOD
        c[i] = b[i - 1] % MOD

    return (a[n] + b[n] + c[n]) % MOD

n = 4
print("Кількість шуканих послідовностей:", count_sequences(n))  # Виведе: 13
