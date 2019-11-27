import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# if stri == "| " == " |" == "| ":
#        newNum = curNum

w, h = [int(i) for i in input().split()]


def direction(line, Contain, Ways):
    for key, value in Contain.items():
        curNum = value

        if curNum == 0:
            Ways[key] = line[curNum:curNum + 2]
        elif curNum == w:
            Ways[key] = line[curNum - 1:curNum + 1]
        else:
            Ways[key] = line[curNum - 1:curNum + 2]

    for key, value in Ways.items():
        stri = value
        if stri == "|-" or stri == " |-":
            Contain[key] = Contain[key] + 3
        elif stri == "-|" or stri == "-| ":
            Contain[key] = Contain[key] - 3
        elif stri == "| " or stri == " |" or stri == "| ":
            Contain[key] = Contain[key]

    return Contain


Contain = {}
Ways = {}
for i in range(h):
    line = input()
    # print(i)
    if i == 0:
        start = list(range(0, w, 3))

        for i in start:
            Contain[line[i]] = i
            Ways[line[i]] = ""

    print(i)
    if i > 0 and i < h - 1:
        Contain = direction(line, Contain, Ways)

    if i == (h - 1):
        for key, value in Contain.items():
            # print(Contain)
            print(str(key) + line[value])  # +line[curNum]

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
