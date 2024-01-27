#Write a code to find the factorial of a number 
#define a function called factorial
def factorial(n):
#factorial of 0 is 1
    if n==0:
        return 1
    #return n*factorial of n-1 that is (n-1)*factorial of n-2
    else:
        return n * factorial(n-1)
#testing

a=2
result=factorial(a)
print(f'factorial of {a} is {result}')