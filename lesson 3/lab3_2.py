import sys

num = int(sys.argv[1])
elem0 = 0
elem1 = 1
for i in range(num):
   elem0+=elem1
   elem0, elem1 = elem1, elem0
print(elem0)
