#!/usr/bin/env python3

input_1 = [int(i) for i in input().split(' ')]
M = input_1[0]
N = input_1[1]

# if M is even
if M % 2 == 0:
    print(M//2 * N)
    
elif N % 2 == 0:
    print(N//2 * M)

else:
    a = max(M, N)//2 * min(M, N)
    b = min(M, N)//2
    print(a + b)



