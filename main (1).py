import math
from functools import reduce

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def find_lcm(numbers):
    return reduce(lcm, numbers)


p = int(input())  
numbers = list(map(int, input().split()))


if len(numbers) != p:
    print("Помилка: кількість чисел не відповідає p")
else:
    print(find_lcm(numbers))
