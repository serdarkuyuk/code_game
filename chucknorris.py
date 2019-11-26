import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
res=""
for i in message:
    res += bin(ord(i))[2:].zfill(7)

ans = ""
dum = ""
for k in res:
    if k == "1" != dum:
        ans += " 0 "
        dum = "1"
    elif k == "0" != dum:
        ans += " 00 "
        dum = "0"
    ans += "0"

print(ans.strip())