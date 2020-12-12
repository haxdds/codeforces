

arg = [int(i) for i in input().split(' ')]

k = arg[0]
n = arg[1]
w = arg[2]

dollars_needed =((w * (w + 1) // 2) * k) - n

print(dollars_needed if dollars_needed > 0 else 0)


