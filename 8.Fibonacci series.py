#0,1,1,2,3,5,8,13,21 this is an example of fibonacci series here is the code to generate fibonacci series
def fibonacci(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        for i in range(2,n):
            print(a)
            print(b)
            c=a+b
            a=b
            b=c
            print(c)

