# Write a python program check if a string is a palindrome 
#define a function called palindrome pass varible string
def palindrome(string):
    #create attribute namd reverse_string
    reverse_string=string[::-1]
    return reverse_string==string
#test function 
word="mad"
if palindrome(word):
    print(f'{word} is palindrome')
else:
    print(f"{word} is not a palindrome")