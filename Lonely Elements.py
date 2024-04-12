# Given an array of integers, where all elements but one occur twice, find the unique element.
#only possible if one lonely and others occurs most twice or divide of two

a=[1,22,33,22,33,4,4,5,5,5,5,6,6,1,9]
r=0

for i in a:
    r^=i
print(i)
