import math
x1 = 1.1
x = x1
y1 = 6+3*math.cos(x)
print(x1, y1)

dy = -3*math.sin(x)
print(x, dy)

x2 = x + 1e-3
x = x2
y2 = 6+3*math.cos(x)

print(x2, y2)
slope = ((y2 - y1)/(x2 - x1))
print("slope =", slope)

