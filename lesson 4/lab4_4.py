import sys
count = 0
a1 = int(sys.argv[1])
a2 = int(sys.argv[2])

for i in range(a1, a2 + 1):
    a = i%10 + int(i/10)%10 + int(i/100)%10
    b = int(i/1000)%10 + int(i/10000)%10 + int(i/100000)%10
    if (a == b):
        count+=1
print(count)
