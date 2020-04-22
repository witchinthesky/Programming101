import sys
count = 0
line = sys.argv[1]
for i in line:
    if(i == '('):
        count+=1
    elif(i == ')'):
        count-=1
    if(count < 0):
        break
if(count != 0): 
    print("NO")
else:
    print("YES")
