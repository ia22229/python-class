num1 = int(input("Please enter a number : "))
if num1 % 2 == 0 :
    if num1 % 3 == 0 :
        print("Number is divisible by 2 and 3")
    else :
        print("Number is divisible by 2 but not 3")
elif num1 % 3 == 0 :
    print("Number is divisible by 3 not 2 ")
else :
    print("Number is not divisible by 3 and 2")
    
    
    
    
num2 = int(input("Please enter a positive number : "))
if num2 >= 0 :
    if num2 % 2 == 0 :
        print("\nNumber is positive and even")
    else :
        print('\nNumber is positive and odd')
else :
    print("\nNumber is negative")
    
    
    
    
year = int(input('Enter the year : '))
if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 ==0:
            print("\nYear is leap year ", year)
        else :
            print("\nYear is not leap year ", year)     
    else :
        print("\nYear is leap year ", year)
else :
    print("\nYear is not leap year ", year)
    
    
    

n1 = int(input("Enter the number of working days    : "))
n2 = int(input("Enter the number of worked days     : "))
percentage = (n2 / n1) * 100
print( "\nPercentage of worked days is ", percentage)
if percentage >= 75 :
    print("\nYou are eligible for attending exam" )
else :
    print("\nYou are not eligible for attending exam")