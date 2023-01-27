a = float(input("Enter Lower Limit:"))

b = float(input("Enter Upper Limit:"))

x = a
ya = x ** 2 - 5 * x + 6

x = b
yb = x ** 2 - 5 * x + 6

if not (((ya > 0) and (yb < 0)) or ((ya < 0) and (yb > 0))):

    print("Solution does not lies between the given range")
else:
    yc = 1

while (yc != 0):

    c = (a + b) / 2

    yc = c ** 2 - 5 * c + 6

    if ((ya > 0) and (yc < 0)) or ((ya < 0) and (yc > 0)):
        b = c
    if ((yb > 0) and (yc < 0)) or ((yb < 0) and (yc > 0)):
        a = c
print(c)


