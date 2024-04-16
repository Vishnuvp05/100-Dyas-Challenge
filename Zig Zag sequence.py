def ZigZagSequence(a,n):
    a.sort()
    mid=int((n+1)/2)-1
    a[mid],a[n-1]=a[n-1],a[mid]

    st=mid+1
    ed=n-2
    while st<=ed:
        a[st],a[ed]=a[ed],a[st]
        st+=1
        ed-=1

    for i in range(n):
        if i==n-1:
            print(a[i])
        else:
            print(a[i],end=' ')
    return

a=[1,3,2,4,5,6,7]
n=7
ZigZagSequence(a,n)