# while True:
#     try:
#         num = int(input("Enter: "))
#         print(num)
#         break
#     except Exception as err:
#         print("Please enter only numbers")

# try:
#     num = 5 / 2
#     print(num)
#
# except Exception as e:
#     print(e)
#
# finally:
#     print("Finally block runs")

try:
    num = 10 / 0
    print(num)
except ZeroDivisionError:
    print("Doesn't Divide by Zero")
finally:
    print("Exception handled")