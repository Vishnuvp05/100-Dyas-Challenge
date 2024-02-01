# this is the in efficient method that uses nested loops so complexityis O(n^2)
def common1():
    for i in list1:
        for j in list2:
            if i==j:
                return True


#efficient way that uses O(n) complexity
def common(list1,list2):
#create a dictionary
    my_dict={}
    #useing for loop to iterate thriugh list 1
    for i in list1:
       # add the items in my_dict
        my_dict[i]=True
    #for loop to iterate list 2
    for j in list2:
        #if the data in my_dict
        #return True 
        if j in my_dict:
            return True
    #if no common return False
    return False

list1=[1,2,5]
list2=[3,4,5]
print(common(list1,list2))