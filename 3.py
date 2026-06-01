num1=5
num1+=1
print(num1)

num2=6
num2-=1
print(num2)

num3= 7
num3*=2
print(num3)

num4= 8
num4/=2
print(num4)

num5= 9
num5//=2
print(num5)

num6= 10
num6**=2
print(num6)

print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= 50)
print(num1 <= 50)

print(num1 > 0 and num2 > 0)
print(num1 > 0 or num2 > 0)
print(not(num1 > 0 and num2 > 0))
print(not(num1 > 0 or num2 > 0))

num7= int(input("Enter your first number :") )
num8= int(input("Enter your second number :") )
if num7 == num8:
    print("Numbers are equal")
else:
    print("Numbers are not equal")
    
if num7 > num8:
    print("num7 is greater than num8")
else:
    print("num7 is less than or  equal to num8")
    
num9= int(input("Enter your number to check if it's odd or even :") )
if num9 % 2 == 0:
    print("Even number",num9)
else:
    print("Odd number",num9)
    
num10= int(input("Enter your age :") )
if num10 >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
    
num11= int(input("Enter your number to check divisibility by 2, 3 or 5 :") )
if num11 % 2 == 0:
    print("number is divisible by 2")
elif num11 % 3 == 0:
    print("number is divisible by 3")
elif num11 % 5 == 0:
    print("number is divisible by 5")
else:
    print("number is not divisible by 2, 3 or 5")
