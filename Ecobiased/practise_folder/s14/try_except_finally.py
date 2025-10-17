# example with error
try:
    x = 10/0
    print("This won't run.")
except ZeroDivisionError:
    print("You can not divide by zero.")
else:
    print("This runs only if no exception")
finally:
    print("This will always run.")

# example with no error
try:
    x = 10/2
    print("result", x)
except ZeroDivisionError:
    print("You can not divide by zero.")
else:
    print("This run when no exceptions.")
finally:
    print("This will always run.")

# example with multiple except

try:
    num = int('abc')
except ZeroDivisionError:
    print("Can not divide by zero.")
except ValueError:
    print("Invalid conversion to int")
else:
    print("This run when no exceptions.")
finally:
    print("cleanup: closing resources")