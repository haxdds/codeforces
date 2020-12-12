#!usr/bin/env python3
t = int(input())

count=0
for i in range(t):
	nums = [int(i) for i in input().split(' ')]
	if sum(nums) >= 2:
		count += 1
print(count)
