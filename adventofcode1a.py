import math
handle = open('adventofcode1q.txt')


def calculateFuel(mass):
	mass= int(mass)
	module = math.floor(mass / 3) - 2
	if module > 0:
		return module
	else:
		return 0
	
modules = list()
for line in handle:
	line.rstrip()
	mass= int(line)
	module = calculateFuel(mass)
	modules.append(module)
	while module > 0 :
		module = calculateFuel(module)
		modules.append(module)
	
print(sum(modules))
	
	