#Decreasing Triangle
n=5
for i in range(n):
    for j in range(i,n):
        print('*',end=' ')
    print()

# * * * * * 
# * * * *
# * * *
# * *
# *

#or

n=5
while n>0:
    print(n*'* ')
    n-=1

# * * * * * 
# * * * *
# * * *
# * *
# *