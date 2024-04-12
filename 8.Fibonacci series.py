#0,1,1,2,3,5,8,13,21 this is an example of fibonacci series here is the code to generate fibonacci series
def fibonacci(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            
            c=a+b
            a=b
            b=c
            print(c)

fibonacci(10)


#printing as a list

def fibonacci(n):
    f=[]
    a=0
    b=1
    if n==1:
        f.append(a)
    else:
        f.append(a)
        f.append(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            f.append(c)
    print(f)

fibonacci(4)


#nth fibonacci number

def fibonacci(n):
    f=[]
    a=0
    b=1
    if n==1:
        f.append(a)
    else:
        f.append(a)
        f.append(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            f.append(c)
    print(f[-1])

fibonacci(100)
