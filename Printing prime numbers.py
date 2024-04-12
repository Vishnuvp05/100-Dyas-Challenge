def is_prime(number):
    # 1 is a not prime so if to selct less than 2
    if number < 2:
        return False
    #for i in range 2 to square root of the number 
    for i in range(2, int(number**0.5) + 1):
    #if the range number is divisable and remainder is zero returns true 
        if number % i == 0:
            return False
    return True

# Test the function

def get_prime(st,e):
    li=[]
    for i in range(st,e+1):
        if is_prime(i):
            li.append(i)
    return li

a=get_prime(0,100)
print(a)

