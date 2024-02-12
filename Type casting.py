'''
    Implicit casting - automatic
    Explicit casting - manually -> inbuilt methods
'''
n1 = 12
n1 = float(n1)
n2 = 10.2
n2 = int(n2)
res = n1 + n2
print(res, type(res))

name = "Ram"
age = 20
print("Hello, I'm " + name + " and my age is " + str(age))
print(type(age))