#!/usr/bin/env python3

n = int(input())
stones = input()

i = 0
count = 0
while i < len(stones):

    current = stones[i]
    j = i + 1

    while j < len(stones) and current == stones[j]:
        count += 1
        j += 1

    i = j

print(count)



