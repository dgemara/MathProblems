import math

a = input('a: ')
b = input('b: ')
c = input('c: ')


determinant = b**2 - 4*a*c

def eqn_solver1 (a, b, c):
    return (-b + math.sqrt(b**2 - 4*a*c))/2*a
def eqn_solver2 (a, b, c):
    return (-b - math.sqrt(b**2 - 4*a*c))/2*a


if determinant > 0:
	numberOfSolutions = 2
	print "The answer has 2 solutions: %d and %d" % (eqn_solver1 (a, b, c), eqn_solver2 (a, b, c))
elif determinant == 0:
	numberOfSolutions = 1
	eqn_solver1 (a, b, c)
	print "The answer has 1 solution: %d" % (eqn_solver2 (a, b, c))
else:
	numberOfSolutions = 0
	print "The equation has no solutions." 

