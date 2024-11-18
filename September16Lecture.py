#Exercise 2 (Practice)
def calculate(num1, num2):
    """
    A four function calculator
    """

    total = num1 + num2
    diff = num1 - num2
    prod = num1 * num2
    quo = num1 / num2

    return total, diff, prod, quo

print(calculate(10,3))


