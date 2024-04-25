# Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array(In Place).
# In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....

# If there are multiple solutions, find the lexicographically smallest one.

# Note:The given array is sorted in ascending order, and you don't need to return anything to make changes in the original array itself.

# Input:
# n = 5
# arr[] = {1,2,3,4,5}
# Output: 2 1 4 3 5
# Explanation: Array elements after 
# sorting it in wave form are 
# 2 1 4 3 5.

# Input:
# n = 6
# arr[] = {2,4,7,8,9,10}
# Output: 4 2 8 7 10 9
# Explanation: Array elements after 
# sorting it in wave form are 
# 4 2 8 7 10 9.



# The idea is to ensure that all even-indexed elements are greater than their adjacent odd-indexed elements.
# We don’t need to worry about the odd-indexed elements; they will automatically fall into place.
# Traverse the even-indexed elements of the input array and perform the following swaps:
# If the current element is smaller than the previous odd-indexed element, swap the previous and current elements.
# If the current element is smaller than the next odd-indexed element, swap the next and current elements.


def convertToWave( n : int, a :list) -> None:
        # code here
        n = len(a)
        for i in range(1, n, 2):
            if i > 0 and a[i - 1] > a[i]:
                a[i], a[i - 1] = a[i - 1], a[i]
            if i < n - 1 and a[i] < a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        return a

n = 6
arr= [2,4,7,8,9,10]
a=convertToWave(n,arr)
print(a)
