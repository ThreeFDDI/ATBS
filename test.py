#!/usr/local/bin/python3

def myfunction(mylist1):
    print(mylist1)
    mylist1=[0,1]
    return mylist1
      
mylist2=[2,3]
mylist1 = myfunction (mylist2)
print(mylist2)
print(mylist1)
