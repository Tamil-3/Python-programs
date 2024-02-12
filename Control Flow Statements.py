# Branching statements - if, if-else, elif, nested if
'''
num = int(input("Enter a number: "))
if num > 0: # true
    print(str(num) + " is positive")
elif num < 0:
    print(str(num) + " is negative")
else:
    print("It is zero.")
'''

num = int(input("Enter a 3-digit number: "))
if num >= 100 and num <= 999:
    if num % 2 == 0:
        print(str(num) + " is a 3-digit even number")
    else:
        print(str(num) + " is a 3-digit odd number")
else:
    print(str(num) + " is not a 3-digit number")