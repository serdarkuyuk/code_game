def follow(x):
    return x + sum(int(c) for c in str(x))


b = int(input())
a = int(input())

while a != b:
    if a < b:
        a = follow(a)
    else:
        b = follow(b)

print(a)


######

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r_1 = int(input())
r_2 = int(input())


def sumation(n):
    tot = 0
    while (n > 0):
        dig = n % 10
        tot = tot + dig
        n = n // 10
    return tot


lis1 = [r_1]
lis2 = [r_2]
for i in range(100000):
    r_1 = r_1 + sumation(r_1)
    lis1.append(r_1)

for i in range(100000):
    r_2 = r_2 + sumation(r_2)
    lis2.append(r_2)

print(min(set(lis1).intersection(lis2)))
