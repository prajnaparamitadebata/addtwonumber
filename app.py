def add_numbers(a, b):
    return a + b
def subtract_numbers(a, b):
    return a - b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result1 = add_numbers(num1, num2)
result2 = subtract_numbers(num1, num2)
print("Sum =", result1)
print("Sub =", result2)