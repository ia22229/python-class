l1=[1,2,"a","b","c","j",6,8,1]
print(l1)
print(len(l1))
print(l1[0])
print(l1[-1])
print(l1[2:5])
l2 = [5,6,7]
print(l1+l2)
print(l2*4)
print(l1.count(1))
print(l1.index('a'))


l2.append('h')
print(id(l2))
print("\n",l2)
l2.insert(1,"y")
print(l2)
print(id(l2))


l2.remove(5)
print(l2)
l2.pop(1)
print(l2)
l2.pop()
print(l2)

l3=[1,58,45,68,98,14,200,154]
l4=['hi','ji','k','iu','fs']
l3.sort()
print(l3)
l3.sort(reverse=True)
print(l3)
l4.sort()
print(l4)
l4.sort(reverse=True)
print(l4)
l2.reverse()
print(l2)


l2.clear()
print(l2)
l2=l3.copy()
print(l2)

t1=('hi','ji','k','l','k','l')
print(t1)
print(len(t1))
print(t1[0])
print(t1[-1])
print(t1[2:5])
t2 = (5,6,7)
print(t1+t2)
print(t2*4)
print(t1.count('k'))
print(t1.index('k'))

person={
    "id":1,
    "name":"Irfan",
    "address" : "edv"
}
print("\n",person)
print(type(person))
person['salary']=1000
print(person)
person.update({'email':'ia9400265514@gmail.com','phone' : 9539261066})
print(person)
person['salary']=15000
print(person)