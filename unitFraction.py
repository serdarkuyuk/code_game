import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

for i in range(1,(n+1)):
    #checks x*y/(x+y) == n
    if n == (n+i)*int(n*(n+i)/i)/(int(n*(n+i)/i)+(n+i)):
        print("1/{} = 1/{} + 1/{}".format(str(n),str(int(n*(n+i)/i)),str(n+i)))

