# add
# substract
# multiply
# divide

print(" select an operation to perform: ")

print("1. add")
print("2. substract")
print("3. multiply")
print("4. divide")

operation = input("Enter operator; ")

# operation = input("Enter operator; ")

if operation == '1':
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print(" the sum is " + str(int(num1) + int(num2)))
elif operation == '2':
    print(" the sum is " + str(int(num1)) - str(int(num2)))
elif operation == '3':
    print(" the multiply is " + num1 * num2)
elif operation == 4:
    print("the divide is " + num1 / num2)
else:
    print("shanice, shutup")
