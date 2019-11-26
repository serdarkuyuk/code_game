import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

#####
#first solution
fun = lambda x: math.radians(float(x.replace(",",".")))

lon = fun(input())
lat = fun(input())
n = int(input())
d = []
adres = []
clomin = 10**20,''
for i in range(n):
    defib = input().split(';')
    lonb,latb=fun(defib[-2]),fun(defib[-1])
    x, y = (lonb - lon) * math.cos((lat+latb)/2), latb - lat
    #adres.append(defib[1])
    d = math.sqrt(x**2+y**2)*6371
    clomin=min(clomin, (d, defib[1]))
print(clomin[1])




###
#Second Solution

lon = float(input().replace(",", "."))
lat = float(input().replace(",", "."))
n = int(input())
d = []
adres = []
for i in range(n):
    defib = input().split(';')
    lonb, latb = float(defib[-2].replace(",", ".")), float(defib[-1].replace(",", "."))
    x, y = (lonb - lon) * math.cos((lat + latb) / 2), latb - lat
    adres.append(defib[1])
    d.append(math.sqrt(x ** 2 + y ** 2) * 6371)

print(adres[d.index(min(d))])