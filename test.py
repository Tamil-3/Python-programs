'''
    2 5
    2 ^ 5 -> 2 * 2 * 2 * 2 * 2
'''

# base = int(input())
# power = int(input())
# res = 1
# for i in range(1, power + 1):
#     res = res * base
# print(res)

'''
    145 -> 1! + 4! + 5!  => 145
    
    1. split the number
    2. find factorial for each digit
    3. add the result of factorial
    4. compare the result
'''

def factorial(n):
    n = int(n)
    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for x in range(1, n + 1):
            fact = fact * x
        return fact

res = 0
num = int(input())
for i in str(num):
    res += factorial(i)

print("Peterson Number" if (res == num) else "Not a Peterson Number")
# if res == num:
#     print("Peterson Number")
# else:
#     print("Not a Peterson Number")

















