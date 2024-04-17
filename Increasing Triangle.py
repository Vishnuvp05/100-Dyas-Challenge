#increasing traingle
n=5
for i in range(n):#row
    for j in range(i+1):#coloumn
        print('*',end='')
    print()
#or

n = 5
while n > 0:
    print(n * '*')
    n -= 1
