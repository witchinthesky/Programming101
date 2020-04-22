import sys

a = str(sys.argv[1])
a = a.lower()
while a.find(' ') != -1:
    a = a[:a.find(' ')] + a[a.find(' ') + 1:]
b = a[::-1]
if a == b: 
    print('YES')
else:
    print('NO')
