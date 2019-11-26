import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


l = sorted([int(input()) for _ in range(int(input()))])
print(l)
print(min((l[i + 1] - l[i] for i in range(len(l) - 1))))

n = int(input())
listss = []
for i in range(n):
    pi = int(input())
    listss.append(pi)

listss.sort()

a = listss[0]
close = 10 ** 10
for i in listss[1:]:
    close = min((i - a), close)
    a = i
print(close)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

