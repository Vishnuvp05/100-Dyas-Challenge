# Longest Common prefix in an array

# Given an array of N strings, find the longest common prefix among all strings present in the array.
# Example 1:

# Input:
# N = 4
# arr[] = {geeksforgeeks, geeks, geek,
#          geezer}
# Output: gee
# Explanation: "gee" is the longest common
# prefix in all the given strings.
# Input: 
# N = 2
# arr[] = {hello, world}
# Output: -1
# Explanation: There's no common prefix
# in the given strings.

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function longestCommonPrefix() which takes the string array arr[] and its size N as inputs and returns the longest common prefix common in all the strings in the array. If there's no prefix common in all the strings, return "-1".


# Expected Time Complexity: O(N*min(|arri|)).
# Expected Auxiliary Space: O(min(|arri|)) for result.


def longestCommonPrefix(self, arr, n):
        # code here
        arr.sort()
        for i in range(len(arr[0])):
            if arr[0][i]!=arr[-1][i]:
                if not arr[0][:i]:
                    return -1
                else:
                    return arr[0][:i]
        return arr[0]