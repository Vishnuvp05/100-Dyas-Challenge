# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
#for eg a=[[1,2,3],
#          [4,5,6],
#          [9,8,9]]
#left to diagonal = 1+5+9   and right to diagonal = 3+5+9   hence the absolute difference is abs(15-17) = 2


def diagonalDifference(arr,n):
    # Write your code here
    left=right=0
    for i in range(n):
        left+=arr[i][i]
        right+=arr[i][n-1-i]
    return abs(left-right)

a=[[1,2,3],
   [4,5,6],
   [9,8,9]]

n=len(a)

a=diagonalDifference(a,n)
print(a)

