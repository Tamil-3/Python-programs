# Decorators

# Python program to illustrate functions
# can be treated as objects
'''
def shout(text):
	return text.upper()

print(shout('Hello'))

yell = shout

print(yell('Hello'))
'''
# -------------------------------------

# Python program to illustrate functions
# can be passed as arguments to other functions
'''
def shout(text):
	return text.upper()

def whisper(text):
	return text.lower()

def greet(func): # func() = shout()  func() = whisper()
	# storing the function in a variable
	greeting = func("""Hi, I am created by a function passed as an argument.""")
	print (greeting)

greet(shout)
greet(whisper)
'''
# ----------------------------------------

# Python program to illustrate functions
# Functions can return another function
'''
def create_adder(x):  # x = 15
	def adder(y): # y = 10
		return x+y

	return adder

add_15 = create_adder(15)  # add_15() = adder()
# print(add_15)
print(add_15(10))
'''
# ---------------------------------------------
'''
def make_pretty(func): # func = ordinary
    # define the inner function
    def inner():
        # add some additional behavior to decorated function
        print("I got decorated")
        # call original function
        func() # ordinary()
    # return the inner function
    return inner

# define ordinary function
def ordinary():
    print("I am ordinary")

# decorate the ordinary function
decorated_func = make_pretty(ordinary) # decorated_func = inner

# call the decorated function
decorated_func()  # inner()
'''
# --------------------------------------------------

def make_pretty(func):

    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty  # Decorator
def ordinary():
    print("I am ordinary")

ordinary()
