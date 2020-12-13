from math import ceil

args = input().split(' ')

n = int(args[0])
m = int(args[1])
a = int(args[2])

# Minimum blocks needed to cover short endi
x = ceil( min(m, n) / a)

y = ceil(max(m, n) / a )

print(x * y)


