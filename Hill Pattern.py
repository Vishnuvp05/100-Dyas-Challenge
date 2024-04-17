#Hill Pattern
#right sided triangle  +increasing triangle
n=5
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i): #here we are changing i+1 to i because to avoif middle repitition
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()

#           * 
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
