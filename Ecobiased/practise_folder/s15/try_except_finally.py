# example with error
try:
    x = 10/0
    print("this won't run")
except ZeroDivisionError:
    print("You can not divide by zero")
else:
    print("This run when no exception")
finally:
    print("This will always run")

# example with no error

try:
    x = 10/2
    print("This will run")
except ZeroDivisionError:
    print("You can not divide by zero")
else:
    print("This run when no exception")
finally:
    print("This will always run")

# example with multiple except

try:
    #num = int('abc')
    num = int('23')
except ZeroDivisionError:
    print("You can not divide by zero")
except ValueError:
    print("Invalid converion to int")
else:
    print("This run when no exception")
finally:
    print("cleanup: closing resources")