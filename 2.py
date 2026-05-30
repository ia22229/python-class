name='irfan' #string data type
print(name) 
print(id(name))


num1=123
num2=1.5
print(id(num1))
print(type(num1))
print(type(num2))


num3= int(input("Enter your number :") )
print(num3)
print(type(num3))

num4= 0
num5= 14
print(bool(num4), bool(num5))

num6= int(input("Enter your number :") )
num7= int(input("Enter your number :") )
print('addition : ',num6+num7,'\nsubtraction : ',num6-num7,'\nmultiplication : ',num6*num7,'\ndivision : ',num6/num7,'\nfloor division : ',num6//num7,'\nmodulus : ',num6%num7,'\npower : ',num6**num7,)

num8= float(input("Enter Breadth : "))
num9= float(input("Enter Length : "))
area= num8*num9
print('Area of rectangle : ',area)
