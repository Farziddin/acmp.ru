import sys
import math

n = int(input())
if n == 0:
    print(0)
else:
    ans = 5527
    for i in input().split():
        r = int(i)
        if abs(ans) > abs(r) or 0 < r == -ans:
            ans = r

    print(ans)
