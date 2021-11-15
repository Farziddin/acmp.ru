import sys
import math

l = int(input())
h = int(input())
t = input().upper()
for i in range(h):
    row = input()
    text = ''
    for x in t:
        if 'A' <= x <= 'Z':
            j = ord(x) - ord('A')
        else:
            j = 26
        text = text + row[(j * l): ((j + 1) * l)]
    print(text)

