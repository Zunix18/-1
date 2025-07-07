import math

def count_intersections(x1, y1, r1, x2, y2, r2):
    d = math.hypot(x2 - x1, y2 - y1)  

    if d == 0 and r1 == r2:
        return -1  
    elif d > r1 + r2:
        return 0  
    elif d == r1 + r2:
        return 1  
    elif abs(r1 - r2) < d < r1 + r2:
        return 2  
    elif d == abs(r1 - r2):
        return 1  
        return 0  


x1, y1, r1, x2, y2, r2 = map(int, input().split())


print(count_intersections(x1, y1, r1, x2, y2, r2))
