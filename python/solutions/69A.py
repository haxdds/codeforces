
n = int(input())

x = []
y = []
z = []

for k in range(n):
    args = input().split(' ')
    x.append(int(args[0]))
    y.append(int(args[1]))
    z.append(int(args[2]))

if sum(x) == sum(y) == sum(z) == 0:
    print("YES")
else:
    print("NO")

