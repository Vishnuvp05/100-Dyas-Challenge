# Given an array of integers, where all elements but one occur twice, find the unique element.

a=[1,22,33,22,33,4,4,5,5,5,5,6,6,1,9]
r=0

for i in a:
    r^=i
print(i)