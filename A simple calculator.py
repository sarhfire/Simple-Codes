# Simple-Codes
print("Select an option")
print("1. Add")
print("2. Subtract")
print("3. Divide")
print("4. Multiply")
print("5. Square root")

# The root code of the program
operation = int(input())

if operation == "1":
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter second number"))
    print("The sum is " + str(int(num1) + int(num2)))

elif operation == "2":
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter second number"))
    print("The difference is " + str(int(num1) - int(num2)))

elif operation == "3":
    num1 = int(input("Enter first  number"))
    num2 = int(input("Enter second number"))
    print("The Product is " + str(int(num1) / int(num2)))

elif operation == "4":
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter second number"))
    print("The product is " + str(int(num1) * int(num2)))

elif operation == "5":
    # Square root been imported
    import math
    num = int(input("Enter number"))
    ans = math.sqrt(num)
    print("The square root is ", ans)
