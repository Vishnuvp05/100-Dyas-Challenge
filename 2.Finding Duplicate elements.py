   # Create an empty set to store unique elements
def containsDuplicate(nums):  
    seen = set()
    
    # Iterate through the array
    for num in nums:
        # If the element is already in the set, it's a duplicate
        if num in seen:
            return True
        # Otherwise, add it to the set
        seen.add(num)
    
    # No duplicates found
    return False