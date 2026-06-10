person={
    "id":1,
    "name":"Irfan",
    "address" : "edv",
    'phone' : 1234567890,
    "salary" : 50000
}
print(person)
person.pop('phone')
print(person)
person.popitem()
print(person)
print(person.keys())
print(person.values())  
print(person.items())
person['First Name'] = person.pop('name')

s1 = {
    'apple' , 'grapes' , 'banana' , 1 , 2 , 3 , 4 ,'orange'
}
s1.add('kiwi')
print(s1)
s1.update(['mango','papaya'])
print(s1)
s1.remove('banana')
print(s1)
s1.discard('grapes')
print(s1)
s1.discard('grapes')
print(s1)

s2 = {'abc' , 'def' , 'ghi' , 1 , 2 , 3}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))

a = [1,2,3,4,5]
b= [6,7,8,9,10]

print( 1 in a)
print(10 in a)
print(10 not in a)

z=a

print(a==z)
print(a is b)
print(a is not b)
print(a is z)

str= "python programming"
if('a' in str):
    print("a is present in the string")
else:
    print("a is not present in the string")

i = 0
while i < 5:
    print(i)
    i += 1
    
    
i=1
while i <= 50:
    if i % 2 == 0:
        print(i)
    i += 1
    
i=1
sum=0
while i<=10:
    sum += i
    i += 1
print("The sum of first 10 natural numbers is: ", sum)


i=1
evenc = 0
oddc =0
while i < 100:
    if i % 2 == 0:
        evenc+=1
    else :
        oddc+=1
    i+=1
print('Even Count is ', evenc ,' Odd count is ', oddc )