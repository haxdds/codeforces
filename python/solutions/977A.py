

args = input().split(' ')

n = int(args[0])
k = int(args[1])

for count in range(k):

    if n % 10 != 0:
        n -= 1
    else:
        n = n // 10


print(n)






