# Additional funtionality and UX was added whilst waiting for this to be reviewed
from os import system

print("Simple calculator app.\n")
print("Add: + | Subtract: - | Multiply: * | Divide: / | Power: ^\n")
print("Please select an option from the list below.")
status = True

while status == True:
    # Menu
    print("\n1. Console Calculation")
    print("2. File Calculation")
    print("0. Exit\n")
    user_choice = str(input("Please enter the option number: "))

    # Uses console input
    if user_choice == '1':
        system('cls')
        console_calculator = True
        print("Add: + | Subtract: - | Multiply: * | Divide: / | Power: ^")
        with open("T10/calculator_log.txt", 'a') as log:
            print("\nYour calculations will be written to a text file upon exiting the app.")
            print("To return to the menu enter 'q' as the operator.\n")
            while console_calculator == True:
                try:
                    number1 = float(input('Please enter the first number: '))
                    number2 = float(input('Please enter the second number: '))
                    operator = input('Please enter the operator: ')
                    if operator == "+":
                        result = number1 + number2
                        print("{} + {} = {}\n".format(number1, number2, result))
                        log.write("{} + {} = {}\n".format(number1, number2, result))
                    elif operator == "-":
                        result = number1 -number2
                        print("{} - {} = {}\n".format(number1, number2, result))
                        log.write("{} - {} = {}\n".format(number1, number2, result))
                    elif operator == "/":
                        # Logic to exclude zero division errors
                        if number2 == 0:
                            print("Zero Division Error: You cannot divide by zero, please try again.\n")
                            log.write("Zero Division Error: You cannot divide by zero, please try again.\n")
                        else:
                            result = number1 / number2
                            print("{} / {} = {}\n".format(number1, number2, result))
                            log.write("{} / {} = {}\n".format(number1, number2, result))
                    elif operator == "*":
                        result = number1 * number2
                        print("{} * {} = {}\n".format(number1, number2, result))
                        log.write("{} * {} = {}\n".format(number1, number2, result))
                    elif operator == "^":
                        result = number1 ** number2
                        print("{} ^ {} = {}\n".format(number1, number2, result))
                        log.write("{} ^ {} = {}\n".format(number1, number2, result))
                    # Return to menu logic
                    elif operator.lower() == 'q':
                        log.close()
                        system('cls')
                        console_calculator = False

                    # Catch for invalid operators
                    else:
                        print("Invalid Operator: That operator does not exist, please try again.\n")
                        log.write("Invalid Operator: That operator does not exist, please try again.\n")

                # Catch for invalid values
                except ValueError:
                    print("Value Error: You have entered an invalid value, please try again.\n")
                    log.write("Value Error: You have entered an invalid value, please try again.\n")

    # Uses text file as input, tested using file input 'T10/calc_test_data.txt'
    elif user_choice == '2':
        system('cls')
        print("Add: + | Subtract: - | Multiply: * | Divide: / | Power: ^\n")
        file_calc = True
        print('Please ensure that each calculation is on a new line and each element separated by a space.')
        print('e.g. 32 * 24')
        print("The results of your calculations uill be printed here.\n")
        while file_calc == True:
            user_file = input("Please enter the name of the text file or q to return to the menu: ")
           
            # Return to menu logic
            if user_file.lower() == 'q':
                system('cls')
                file_calc = False
                break

            print("\n")
            try:
                with open(user_file, 'r') as file:
                    with open('T10\calculator_log.txt', 'a') as log:
                        for line in file:
                            # Split at the new lines in the file
                            line = line.split('\n')
                            # Split the equation into a list of component parts
                            line = line[0].split(' ')
                            try:
                                number1 = float(line[0])
                                number2 = float(line[2])
                                operator = line[1]
                                if operator == "+":
                                    result = number1 + number2
                                    print("{} + {} = {}\n".format(number1, number2, result))
                                    log.write("{} + {} = {}\n".format(number1, number2, result))
                                elif operator == "-":
                                    result = number1 -number2
                                    print("{} - {} = {}\n".format(number1, number2, result))
                                    log.write("{} - {} = {}\n".format(number1, number2, result))
                                elif operator == "/":
                                    # Logic to excude zero division errors
                                    if number2 == 0:
                                        print("Zero Division Error: You cannot divide by zero, please try again.\n")
                                        log.write("Zero Division Error: You cannot divide by zero, please try again.\n")
                                    else:
                                        result = number1 / number2
                                        print("{} / {} = {}\n".format(number1, number2, result))
                                        log.write("{} / {} = {}\n".format(number1, number2, result))
                                elif operator == "*":
                                    result = number1 * number2
                                    print("{} * {} = {}\n".format(number1, number2, result))
                                    log.write("{} * {} = {}\n".format(number1, number2, result))
                                elif operator == "^":
                                    result = number1 ** number2
                                    print("{} ^ {} = {}\n".format(number1, number2, result))
                                    log.write("{} ^ {} = {}\n".format(number1, number2, result))
                                
                                # Catch for invalid operators
                                else:
                                    print('Invalid Operator: That operator does not exist, please try again.\n')
                                    log.write('Invalid Operator: That operator does not exist, please try again.\n')
                            
                            # Catch for invalid values
                            except ValueError:
                                print("Value Error: You have entered an invalid value, please try again.\n")
                                log.write("Value Error: You have entered an invalid value, please try again.\n")
                                continue
                file.close()

            # Catch for missing file
            except FileNotFoundError:
                print('This file does not exist, please try again.\n')

    # Exit logic
    elif user_choice == '0':
        system('cls')
        status = False

    # Catch for invalid menu selection
    else:
        print("Invalid selection, please try again")
