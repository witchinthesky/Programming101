import sys
import math

x = int(sys.argv[1])
y = int(sys.argv[2])
z = bool(sys.argv[3])
line = 'la-'*x
line = line[:-1]
line +=' '
line = line * y
line = line[:-1]
if z: 
   line +='!'
else:
   line+='.'
line = "Everybody sing a song: " + line
print line
