import math


def is_prime(num: int):
    for k in range(2, int(math.sqrt(num) + 1)):
        if num % k == 0:
            return False
    return True


t = s = 0
for x in input().split():
    x = int(x)
    if is_prime(x):
        t = t + 1
        s = s + x

print(s)
print("Yes" if t > 2 else "No")
