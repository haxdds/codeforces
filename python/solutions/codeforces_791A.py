

arg = input().split(' ')

a = int(arg[0])
b = int(arg[1])

years = 0

while a <= b:
    years += 1
    a = a * 3
    b = b * 2

print(years)

