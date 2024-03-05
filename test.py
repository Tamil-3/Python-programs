'''
    543544 -> 5 => 4
    abc123 -> 3

    num = 543544
n = 5
count = 0

for i in str(num):
    if i != str(n):
        count += 1
print(count)

str1 = "a1b2c3123"
count = 0

for i in str1:
    if i >= '0' and i <= '9':
        count += 1
print(count)
'''


list1 = []
no_of_input = int(input("Enter a no of input: "))

for i in range(no_of_input):
    num = int(input())
    list1.append(num)
print(list1)











