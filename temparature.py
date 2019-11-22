
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = 6  # the number of temperatures to analyse
mylist = [2, -2, 4, -5, -6, 7]
if n == 0:
    print(str(0))
di1 = 5526
for i in mylist:
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    if t > 0:
        di = t
    else:
        di = -t

    if di < di1:
        di1 = di
        p = t
    elif di == di1:
        p = abs(t)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(p)