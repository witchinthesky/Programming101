import sys
size = len(sys.argv) - 1
line = sys.argv[size];
for i in range(size - 1, 1, -1):
    line += ' ' + sys.argv[i]
if size > 1: 
    line += ' ' + sys.argv[1]
print (line)
