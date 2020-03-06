def recursive_factorial(number):
    if number == 1:
        return number
    else:
        return number * recursive_factorial(number - 1)


number = int(input("Enter integer: "))
print("Result = " + str(recursive_factorial(number)))
