#!/usr/bin/env python3

matrix = []

for x in range(5):
    row = [int(x) for x in input().split(' ')]
    matrix.append(row)

i_1 = 0 
j_1 = 0

i_center = 2
j_center = 2

delta_i = 0
delta_j = 0

for row in matrix:
    
    if 1 in row:
        for x in row:
            if x != 1:
                j_1 += 1
            else:
                delta_j = j_center - j_1
        delta_i = i_center - i_1
    else:
        i_1 += 1

print(abs(delta_i) + abs(delta_j))

