#!/usr/bin/env python3

expression = input().split('+')

expression.sort()

print("".join(str(x) + "+" for x in expression)[:-1])
