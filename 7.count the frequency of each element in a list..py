def count_frequency(numbers):
   frequency = {}
   for num in numbers:
    # Check if the element is already a key in the frequency dictionary
    if num in frequency:
        # If yes, increment its value by one
        frequency[num]+=1
    else:
        # Create a new key-value pair with the element as the key and one as the value
       frequency[num]=1
   return frequency

# Test the function
nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
frequency_count = count_frequency(nums)
print(frequency_count)


a=[1,3,22,12,3,11,3,1,3,1,1]

b={}

for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1

maxi=max(b,key=b.get)
print(b)

#or

max_val=float('-inf')
max_key=None

for key,value in b.items():
    if value>max_val:
        max_val=value
        max_key=key

print(max_key,max_val)
