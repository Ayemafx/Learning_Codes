class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def __add__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        return Fraction(newnum, newden)

    def __eq__(self, other):
        if self.num == other.num and self.den == other.den:
            return True
        else:
            return False


f1 = Fraction(3, 4)
f2 = Fraction(6, 4)
print(f1+f2)
print(f1/f2)
print(f1 == f2)

