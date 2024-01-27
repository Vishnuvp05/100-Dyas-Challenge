#Write a code to find the Largest number in a listr 
#define a function called Largest
def largest(numbers):
    # create an attribute big and store first value of big their
    big=numbers[0]
    # to compare all values with big create  a loop and if num>big it returns big 
    for num in numbers:
        if num>big:
            big=num
    return big

a=[1,2,3,4,10,9,8]
b=largest(a)
print(f'The largest number in a list{a} is {b} ')
