# l1 = [2, "Python", [12, 14, 16], ['a']]
# print(type(l1))
# print(l1[2])
# print(l1[2][1])
# print(l1[3][0])

'''
l1 = [10, 20, 12, 34, 56]
print(l1[-3])
# Slicing
print(l1[1:4])
print(l1[2:])
print(l1[:4])
print(l1[-5:-3])
'''
'''
l1 = [10, 20, 12, 34, 56]
print(l1)
l1[3] = 27
print(l1)
l1[1:4] = [11, 12, 13]
print(l1)
'''
# append and extend
'''
l2 = [10, 20, 30, 40, 50]
l2.append(60)
print(l2)

l2.extend([52, 53])
print(l2)

l2.insert(0, 1)
print(l2)

list1 = [1, 2]
list2 = [1, 'a', 'b']
print(list1 + list2)
'''
# remove elements
'''
l2 = [10, 20, 30, 40, 50]
l2.remove(30)
print(l2)
l2.pop()
print(l2)
l2.pop(1)
print(l2)
'''

# Tuple
t1 = (12, 2.4, "Tuple", True)
print(t1)
l1 = list(t1)
print(l1)
t1 = tuple(l1)
print(type(t1))











