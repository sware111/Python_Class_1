# Calculator Projects

while True:
    choose = input("1 >>>> int\n2 >>>> float\n3 >>>> exit\nChoose: ")

    if choose == "1":
        choose_operation = input("Choose your Operation(+,-,*,/,//,**): ")
        number1 = int(input("Enter Number One : "))
        number2 = int(input("Enter Number Two : "))
        
        if choose_operation not in "+,-,*,/,//,**":
            print("Invalid Operator,try again! ")

        else:
            if choose_operation == '+':
                print(f"integer one is {number1}, and integer two is {number2}, and result of sum is: {number1 + number2}")

            if choose_operation == '-':
                print(f"integer one is {number1}, and integer two is {number2}, and result of difference is: {number1 - number2}")

            if choose_operation == '*':
                print(f"integer one is {number1}, and integer two is {number2}, and result of multiple is: {number1 * number2}")

            if choose_operation == '/':
                if number2 == 0:
                    print("Invalid input number! please enter number again")
                else:
                    print(f"integer one is {number1}, and integer two is {number2}, and result of float_division is: {number1 / number2}")

            if choose_operation == '//':
                if number2 == 0:
                    print("Invalid input number! please enter number again")
                else:
                    print(f"integer one is {number1}, and integer two is {number2}, and result of float_division is: {number1 // number2}")

            if choose_operation == '**':
                print(f"integer one is {number1}, and integer two is {number2}, and result of power is: {number1 ** number2}")

    elif choose == "2":
        choose_operation = input("Choose your Operation(+,-,*,/,//,**): ")
        number1 = float(input("Enter Number One : "))
        number2 = float(input("Enter Number Two : "))

        if choose_operation not in "+,-,*,/,//,**":
            print("Invalid Operator, please enter your operator(+,-,*,/,//,**): ")
            
        else:
            if choose_operation == '+':
                print(f"integer one is {number1}, and integer two is {number2}, and result of sum is: {number1 + number2}")

            if choose_operation == '-':
                print(f"integer one is {number1}, and integer two is {number2}, and result of difference is: {number1 - number2}")

            if choose_operation == '*':
                print(f"integer one is {number1}, and integer two is {number2}, and result of multiple is: {number1 * number2}")

            if choose_operation == '/':
                if number2 == 0:
                    print("Invalid input number! please enter number again")
                else:
                    print(f"integer one is {number1}, and integer two is {number2}, and result of float_division is: {number1 / number2}")

            if choose_operation == '//':
                if number2 == 0:
                    print("Invalid input number! please enter number again")
                else:
                    print(f"integer one is {number1}, and integer two is {number2}, and result of float_division is: {number1 // number2}")

            if choose_operation == '**':
                print(f"integer one is {number1}, and integer two is {number2}, and result of power is: {number1 ** number2}")
    elif choose == "3" or "q" or "Quit" or "quit":
        break