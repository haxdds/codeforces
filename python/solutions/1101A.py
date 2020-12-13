from math import ceil

q = int(input())


for k in range(q):

    args = input().split(' ')
    l = int(args[0])
    r = int(args[1])
    d = int(args[2])
    
    if (l-1) / d >= 1:
        print(d)
    else:
        print(ceil( (r + 1) / d) * d)   



