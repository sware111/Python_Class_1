# Calculator 
print("Welcome to my Calculator".center(150))

choose = input("1 >>>> int or 2 >>>> float :")

# input int number
if choose == "1":
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
elif choose == "2":
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