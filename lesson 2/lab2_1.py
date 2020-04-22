import sys
import math
x = float(sys.argv[1])
u = float(sys.argv[2])
q = float(sys.argv[3])
result = 1/float(q*math.sqrt(2*math.pi))*math.exp(-1*float(x-u)**2/(2*q**2))
print result
