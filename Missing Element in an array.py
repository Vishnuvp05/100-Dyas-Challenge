# Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.

def missing(array,n):
    expected_sum=n*(n+1)//2
    actual=sum(array)
    return expected_sum-actual

array=[1,2,3,5]
n=5
a=missing(array,n)
print(a)