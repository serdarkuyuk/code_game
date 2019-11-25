import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input().upper()

# find the location of characters and put in to a list
starts = []
for k in t:
    pos = (ord(k) - 65) * l
    if pos < 0:
        starts.append(104)
    else:
        starts.append(pos)

# create a all rows
raw = []
for i in range(h):
    raw.append(input())

# write to console
for i in range(h):
    for num in starts:
        # kt.append(raw[i][num:num+4])
        print(raw[i][num:num + l], end='')
    print()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
