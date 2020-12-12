#!/usr/bin/env python3

n = int(input())


x = 0

for t in range(n):
    s = input()

    if '++' in s:
        x += 1
    elif '--' in s:
        x -= 1

print(x)
