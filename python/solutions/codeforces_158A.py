#!/usr/bin/env python3

input_1 = [int(i) for i in input().split(' ')]

n = input_1[0]
k = input_1[1]

a = [int(i) for i in  input().split(' ')]

a_k = a[k-1]

advancing_participants = [x for x in a if x >= a_k and x > 0]

print(len(advancing_participants))




