# x=100
# def sum():
#     global n
#     n=25
#     print("inside the function n ",n)
#     print("inside the function x ",x)
#     return
# sum()
# print("outside the function x ",x)
# print("outside the function n ",n)




# def inner():
#     print("outer function")
#     def outer():
#         print("inner function")
#     outer()
# inner()




# def wish():
#     msg="good morning"
#     def display():
#         print(msg)
#     display()
# wish()



# def atm():
#     balance=10000
#     def bal():
#         print(f'balance is {balance}')
#     bal()
# atm()


# def shopping():
#     price=500
#     quantity=3
#     def total():
#         return f"Total price is {price*quantity}"
#     print(total())
# shopping()




# x='global'
# def outer():
#     x='enclosed'
#     def inner():
#         x='local'
#         print(x)
#     inner()
#     print(x)
# outer()
# print(x)



# name='irfan'
# def outer():
#     name='ahmed'
#     def inner():
#         print(name)
#     inner()
# outer()



# def demo():
#     print('hello')
#     demo()
# demo()



# def numbers(i):
#     if i<5:
#         return
#     print(i)
#     numbers(i+1) 
# numbers(1)

# def fact(i):
#     global factorial
#     if i==1:
#         return 1
#     return i*fact(i-1)
# print(fact(5))

def fibo(i):
    if i <= 1 :
        return i
    else:
        return fibo(i-1)+fibo(i-2)
    
for i in range(6):
    print(fibo(i),end=" ")
    
    
def fibo(i):
    if i <= 1 :
        return i
    else:
        return fibo(i-1)+fibo(i-2)
    
for i in range(6):
    print(fibo(i),end=" ")
    