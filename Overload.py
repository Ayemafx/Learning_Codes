class cFraction: #c for class
    def __init__(self, Numerator, Denominator):
        self.__numerator = Numerator # __ not present it will be accessible for other programmers too __ means hidden
        # single _ is accessible to those who know
        self.__denominator = Denominator

    # if you define an already defined function it's called overriding, python inherits classes internally

    def __str__(self):
        if self.__denominator == 1:
            return str(self.__numerator)
        else:
            return str(self.__numerator)+"/"+str(self.__denominator)

    def __add__(self, other):
        new_numerator = self.__numerator * other.__denominator + other.__numerator * self.__denominator
        new_denominator = self.__denominator * other.__denominator
        return cFraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.__numerator * other.__denominator - other.__numerator * self.__denominator
        new_denominator = self.__denominator * other.__denominator
        return cFraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.__numerator * other.__numerator
        new_denominator = self.__denominator * other.__denominator
        return cFraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.__numerator * other.__denominator
        new_denominator = self.__denominator * other.__numerator
        return cFraction(new_numerator, new_denominator)
    # make a function for greater and less than

    def __eq__(self, other):
        if self.__numerator == other.__numerator and self.__denominator == other.__denominator:
            return "The fractions are equal"
        else:
            return "The fractions are not equal"


def euclidean(numerator, denominator):
    if numerator < denominator:
        temp = numerator
        numerator = denominator
        denominator = temp

    if numerator % denominator == 0:
        return denominator
    else:
        return euclidean(denominator, numerator%denominator)


p = cFraction(3, 4)
q = cFraction(3, 4)
print(p+q)
print(p * q)
print(p - q)
print(p / q)
print(p == q)
