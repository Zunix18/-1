n = int(input("Введіть натуральне число n: "))

count = 0
for m in range(1, n):
    if n // m == n % m:
        count += 1

print(f"Кількість рівних дільників числа {n}: {count}")
