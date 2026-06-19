# def display(name,age,id):
#     print(f"My name is : {name}, My age is : {age}, My id is : {id}")
#     return
# display("Irfan", 22, 12345)



# def displays(name,age,id):
#     print(f"your name is : {name}, Your age is : {age}, Your id is : {id}")
#     return
# displays(age=22, name="Irfan", id=12345)



# def display(name,age,place="kochi"):
#     print(f"My name is : {name}, My age is : {age}, My place is : {place}")
#     return
# display("Irfan", 22,'Kakkanad')
# display("Irfan", 22)



# def display(*args):
#     print(args)
#     return
# display('pen','pencil','book')



# def display(**kargs):
#     print(kargs)
#     return
# display(name="Irfan" , age=22 , id=12345)


# def sum(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     print(f"sum is {sum}")
    
# sum(12,25,42,30)




# dict ={"name":"Irfan","age":22,"place":"Edv"}
# for i,j in dict.items():
#     print(f"{i}:{j}")


def areat(b,h):
    area=.5*b*h
    return area
def areas(s):
    area=s*s
    return area
def arear(b,h):
    area=b*h
    return area
j=0
n=int(input("1. Triangle\n2.Square\n3.Rectangle \nSelect any option : "))
if n==1:
    b=int(input("Enter Base :"))
    h=int(input("Enter Height :"))
    area=areat(b,h)
elif n==2:
    s=int(input("Enter the Side Lenght :"))
    area=areas(s)
elif n==3:
    b=int(input("Enter Breadth :"))
    h=int(input("Enter Height :"))
    area=arear(b,h)
else :
    print("invalid option selected")
    j=1
if j==0:
    print(f"Area is {area}")
    
    
    # atm withdraw,deposit,balance