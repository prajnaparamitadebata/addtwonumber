
# Input a number
num = int(input("Enter a number: "))
if num <= 0:
    print("not valid")
    # Check whether the number is odd or even
elif num % 2 == 0:
    print(num, "is an Even number")
else:
    print(num, "is an Odd number")
