# #Equilllibrium point

# Given an array A of n non negative numbers. The task is to find the first equilibrium point in an array. Equilibrium point in an array is an index (or position) such that the sum of all elements before that index is same as sum of elements after it.

# Note: Return equilibrium point in 1-based indexing. Return -1 if no such point exists.

# Example 1:

# Input: 
# n = 5 
# A[] = {1,3,5,2,2} 
# Output: 
# 3 
# Explanation:  
# equilibrium point is at position 3 as sum of elements before it (1+3) = sum of elements after it (2+2). 

# Example 2:

# Input:
# n = 1
# A[] = {1}
# Output: 
# 1
# Explanation:
# Since there's only element hence its only the equilibrium point

# Your Task:
# The task is to complete the function equilibriumPoint() which takes the array and n as input parameters and returns the point of equilibrium. 

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)


def equilibriumPoint(self,A, N):
        # Your code here
        total=sum(A)
        left=0
        for i in range(N):
            total-=A[i]
            if left==total:
                return i+1
            left+=A[i]
        return -1