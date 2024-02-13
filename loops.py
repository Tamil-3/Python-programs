# loops - for, while
# DRY - Don't Repeat Yourself
# range(start, stop, step)
# for i in range(3, 11, 2):
#     print(i)
'''
sum = 0
for x in range(2, 11, 2):
    sum = sum + x
print(sum)
'''
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
'''
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    res = i * num
    print(res)
    i += 1
'''
# Nested Loops
'''
for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=' ')
    print()
'''

for i in range(1, 10):
    if(i == 5):
        # break
        continue
    print(i)
print("Program end...")













