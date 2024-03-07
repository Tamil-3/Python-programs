'''
    2 5
    2 ^ 5 -> 2 * 2 * 2 * 2 * 2
'''

base = int(input())
power = int(input())
res = 1
for i in range(1, power + 1):
    res = res * base
print(res)