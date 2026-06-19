# fun=lambda :print('hellooo')
# fun()

# func=lambda :'hii'
# print(func())

# funct=lambda n1,n2:n1*n2
# print(funct(3,3))

# h=lambda n1,n2 : 'num2 is greater'if n1<n2  else 'num1 is greater'
# print(h(3,2))

# n1=int(input("Enter a number : "))
# k=lambda n1 : 'Number is even'if n1%2==0 else 'Number is odd'
# print(k(n1))


# n2=int(input("Enter a number : "))
# j= lambda n1 : print("number is positive")if n1>0 else print("number is negative") if n1<0  else print("number is zero")
# j(n2)

# n3=int(input("Enter your age : "))
# j= lambda n1 : print("Child")if n1<13 else print("Teenanger") if n1<20  else print("Adult")
# j(n3)

# l1=[1,52,42,77,87,20,15,30,21,62,63,74]
# even=list(filter(lambda n:n%2==0,l1))
# print(even)

# l2=[1,2,42,7,8,3,15,30,21,6,63,74]
# greater=list(filter(lambda n:n>10,l2))
# print(greater)

# word=['abc','apple','efgh','book','box','pen']
# l3=list(filter(lambda n:len(n)>3,word) )
# print(l3)

# l2=[1,2,42]
# l4=list(map(lambda n:n*2,l2))
# print(l4)

# word=['abc','apple','efgh','book','box','pen']
# l3=list(map(lambda n:n.upper(),word) )
# print(l3)

# from functools import *
# l2=[1,2,42,7,8,3,15,30,21,6,63,74]
# sum=reduce(lambda x,y:x+y,l2)
# print(sum)

from functools import *
l2=[1,2,42,7,8,3,15,30,21,6,63,74]
sum=reduce(lambda x,y:x if x>y else y,l2)
print(sum)