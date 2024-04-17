#Decreasing right sided traingle 
#which is a combination of increasing space and decreasing traingle
n=5
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print()
    