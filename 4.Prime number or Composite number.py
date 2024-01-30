def is_prime(number):
    if number < 2:
        return True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return True
    return False

# Test the function
num = 7
if is_prime(num):
    print(f"{num} is not a composite number")
else:
    print(f"{num} is prime number")