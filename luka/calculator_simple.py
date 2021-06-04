print("Welcome to calculator!\nPlease enter the operation [1-4]:")

while True:
    op = int(input('[1] Addition\n[2] Subtraction\n[3]'
                   'Multiplication\n[4] Division\n[5] EXIT\n'))
    if op == 5:
        print("exiting...")
        quit()

    firstNumber = int(input("please enter your first number: "))
    secondNumber = int(input("Please enter your second number: "))
    answer = 0

    if op == 1:
        answer = firstNumber + secondNumber
    if op == 2:
        answer = firstNumber - secondNumber
    if op == 3:
        answer = firstNumber * secondNumber
    if op == 4:
        answer = firstNumber / secondNumber

    print(answer)
