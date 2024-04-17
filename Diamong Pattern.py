#Diamond Pattern 
#Which is a combinationof hill + reverse hill pattern 

n=5
for i in range(n-1):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i): #here we are changing i+1 to i because to avoif middle repitition
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for  j in range(i,n-1):#we are n-1 instread of n to avoid repetitionin middle  
        print('*',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print()


#           * 
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
#     * * * * * * *
#       * * * * *
#         * * *
#           *

