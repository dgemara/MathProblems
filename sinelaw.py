import math

a = input('Length a: ')
b = input('Length b: ')
c = input('Length c: ')


def angle (a, b, c):
    return math.degrees(math.acos((c**2 - b**2 - a**2)/(-2.0 * a * b)))

angA = angle(a,b,c)
angB = angle(b,c,a)
angC = angle(c,a,b)

assert angA + angB + angC == 180.0

print angA
print angB
print angC
