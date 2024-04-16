#A Teachher asked to open their books toa page number.A student can either start turning pages from the fornt or the back
#They alsways turn one page at a time .When tehy open book page 1 is always on the right side
# |1
#When they flip page 1,they see pages 2,3.Each page execpt the last page will always be printd on both sides.
#The last page may only be printed on front,given the length of the book
#If the book is n pages long, and a student want to turn to page p. What is the minimum no of pages to turn? They can start at the begining or the end of book
#Given n and p.Find the minimum number of pages that must be turned in order to arrive at page p

#Example:
#n=5
#p=3

#  |1  --> 2|3 --> 4|5 
#Using the above diagram if the student want to get to page 3,they open the book to page 1,flip 1 page and they are on the correct page 
#If the open the book form the last page ,page 5 ,they turn 1 page to reach correct page  .  return 1     


def pagecount(n,p):
    front=p//2

    if n%2==1:
        back=(n-p)//2
    else:
        back=(n-p+1)//2
    return min(front,back)


n=6
p=2

a=pagecount(n,p)
print(a)