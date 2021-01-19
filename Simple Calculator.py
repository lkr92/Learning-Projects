run = True

#Simple Calculator that will run on loop upon user request

while run:
    num1 = float(input("Please type a number: "))
    operator = input("Please input an operator character: ")
    num2 = float(input("Please input a second number: "))

    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "/":
        print(num1 / num2)
    elif operator == "*":
        print(num1 * num2)
    else:
     print("Invalid Operator!!")

    if input('Type "yes" for a new request or type anything else to close: ') == "yes" or "Yes" or "YES":
        run = True
    else:
        run = False

print("End of program.")




