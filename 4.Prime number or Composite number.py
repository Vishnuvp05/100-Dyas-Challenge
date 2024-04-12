#define a function named is_prime and pass number
def is_prime(number):
    # 1 is a not prime so if to selct less than 2
    if number < 2:
        return True
    #for i in range 2 to square root of the number 
    for i in range(2, int(number**0.5) + 1):
    #if the range number is divisable and remainder is zero returns true 
        if number % i == 0:
            return True
    return False

# Test the function
num = 7
if is_prime(num):
    print(f"{num} is  a composite number")
else:
    print(f"{num} is prime number")
