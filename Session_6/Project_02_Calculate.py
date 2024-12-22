# Loop the calulate 

# Calculator 
print("Welcome to my Calculator".center(150))

# choose = input("1 >>>> int or 2 >>>> float :")

while True:
    repeat = input("choose your operation(q) or \n 1 >>>> int or 2 >>>> float : ")
    if repeat == "q":
        break

    # input int number
    if repeat == "1":
        operators = input("Choose Operator (+,-,*,/,//,**): ")
        number1 = input("Enter Number 1: ")
        number2 = input("Enter Number 2: ")

        if operators == '+':
            print(f"result is >>>> {int(number1) + int(number2)}")

        elif operators == '-':
            print(f"result is >>>> {int(number1) - int(number2)}")

        elif operators == '*':
            print(f"result is >>>> {int(number1) * int(number2)}")

        elif operators == '/':
            print(f"result is >>>> {int(number1) / int(number2)}")

        elif operators == '//':
            print(f"result is >>>> {int(number1) // int(number2)}")

        elif operators == '**':
            print(f"result is >>>> {int(number1) ** int(number2)}")

    # input float number
    elif repeat == "2":
        operators = input("Choose Operator (+,-,*,/,//,**): ")
        number1 = input("Enter Number 1: ")
        number2 = input("Enter Number 2: ")

        if operators == '+':
            print(f"result is >>>> {float(number1) + float(number2)}")

        elif operators == '-':
            print(f"result is >>>> {float(number1) - float(number2)}")

        elif operators == '*':
            print(f"result is >>>> {float(number1) * float(number2)}")

        elif operators == '/':
            print(f"result is >>>> {float(number1) / float(number2)}")

        elif operators == '//':
            print(f"result is >>>> {float(number1) // float(number2)}")

        elif operators == '**':
            print(f"result is >>>> {float(number1) ** float(number2)}")

    else:
        print("Invalid Number or Operator!")