#Reverse Hill
#which iis reverse right sided triangle + decresing triangle
n=5
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for  j in range(i,n-1):#we are n-1 instread of n to avoid repetitionin middle  
        print('*',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print()


#  * * * * * * * * * 
#     * * * * * * *
#       * * * * *
#         * * *
#           *