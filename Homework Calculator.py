title = "Calculator"
print(title)


x = int(input("x: "))

operation = input("(+, -, * or /): ")

y = int(input("y: "))



if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
else:
    print("You did not provide the correct math operation.")









