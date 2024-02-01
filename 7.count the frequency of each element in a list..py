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