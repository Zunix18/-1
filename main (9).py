import math

def min_steps(x: int, y: int) -> int:
    d = y - x
    if d == 0:
        return 0

    k = int(math.sqrt(d))
    if k * k == d:
        return 2 * k - 1
    elif k * k < d <= k * k + k:
        return 2 * k
    else:
        return 2 * k + 1


examples = [
    (45, 48),
    (45, 49),
    (45, 50),
    (45, 51),
    (45, 45)
]

for x, y in examples:
    result = min_steps(x, y)
    print(f"x = {x}, y = {y} → кроків = {result}")
