data = 'python programming'
print(len(data))
print(data[0])
print(data[1])
print(data[2])
print(data[-1])

print(data[1:17])
print(data[1:])
print(data[:15])
print(data[1:17:2])
print(data[-6:])
print(data[-11:-3])

print(data[::-1])

print("hello"+" world "+data)
data1 = data*3
print(data1)
print("hai"*5)

print(data1.index('y'))
print(data1.count('p'))
print(data.lower())
print(data.capitalize())
print(data.startswith('p'))
print(data.replace('p','w'))

data2 = "python is a programming language"
l1 = data2.split(" ")
print(l1)

age = 10
name = "Alice"
print(f"My name is {name} and I am {age} years old.")

print("hello\nworld")
print("hello\tworld")
print("hello\\world")
print('it\'s a nice day')
print("hello w\bworld")