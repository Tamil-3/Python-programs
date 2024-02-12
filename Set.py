# Set - collection of values
# Not allow duplicates, Unordered
# { }
'''
s1 = {2, 4, 5, 6, "a", 'b', False, 2 ,5}
s2 = {10, 20, 12, 14}
s3 = {1, 4, 12, 20}
print(s2.union(s3))
print(s3.intersection(s2))
print(s2.difference(s3))
'''

# Dictionary -> key - value pair
d1 = {
    "name":"John",
    "age": 25,
    1: 'a',
    "age": 30
}
print(d1)
print(d1[1])
d1["name"] = "Steve"
print(d1.values())
print(d1.keys())

l1 = [(1, 'a'),(2, 'b'), (3, 'c')]
dict1 = dict(l1)
print(dict1)

c = 2 + 3j
print(type(c))