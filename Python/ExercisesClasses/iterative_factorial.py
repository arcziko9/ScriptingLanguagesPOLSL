def iterative_factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


number = int(input("Enter integer: "))
print("Result = " + str(iterative_factorial(number)))
