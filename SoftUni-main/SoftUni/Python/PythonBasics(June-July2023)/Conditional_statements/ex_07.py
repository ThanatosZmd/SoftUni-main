import math
type = str(input())
if type == 'square':
    n = float(input())
    area = n*n
    print(round(area,3))
elif type == 'rectangle':
    a = float(input())
    b = float(input())
    area = a*b
    print(round(area, 3))
elif type == 'circle':
    r = float(input())
    area = math.pi*r*r
    print(round(area, 3))
elif type == 'triangle':
    c = float(input())
    hc = float(input())
    area = (c*hc)/2
    print(round(area, 3))
else:
    pass