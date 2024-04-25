# #Leaders in an array

# Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is a leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader. 

# Input:
# n = 6
# A[] = {16,17,4,3,5,2}
# Output: 17 5 2
# Explanation: The first leader is 17 
# as it is greater than all the elements
# to its right.  Similarly, the next 
# leader is 5. The right most element 
# is always a leader so it is also 
# included.

# Input:
# n = 6
# A[] = {16,17,4,3,5,2}
# Output: 17 5 2
# Explanation: The first leader is 17 
# as it is greater than all the elements
# to its right.  Similarly, the next 
# leader is 5. The right most element 
# is always a leader so it is also 
# included.
# Your Task:
# You don't need to read input or print anything. The task is to complete the function leader() which takes array A and n as input parameters and returns an array of leaders in order of their appearance.

def leaders(self, A, N):
        #Code here
        maxi=float('-inf')
        res=[]
        for i in range(N-1,-1,-1):
            if A[i]>=maxi:
                res.append(A[i])
                maxi=A[i]
        res.reverse()
        
        return res
        