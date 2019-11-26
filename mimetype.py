import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.

q = int(input())  # Number Q of file names to be analyzed.
#print(q)
lookup = {}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    lookup[ext.upper()] =mt
    lookup[ext.lower()] =mt
#print(lookup)
for i in range(q):
    fname = input().lower().split(".")  # One file name per line.

    if len(fname) < 2 or fname[-1] == "":
        print("UNKNOWN")
    else:
        if fname[-1] not in lookup.keys():
            print("UNKNOWN")
        else:
            print(lookup[fname[-1]])

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.

