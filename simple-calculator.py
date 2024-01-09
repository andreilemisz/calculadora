# Code to identify two numbers and an operator, do the math
# and returne a value or an error if the numbers or operator are
# incorret or the division is by 0
# At the end, the user can leave or use the calculator again
import os   # To clear the console
calculator_active = True    # To allow the software to repeat at the end
leave_software = "" # To allow leave or repeat the application
number_1 = 0    # First digit
number_2 = 0    # Second digit
numbers_are_valid = None    # Variable to determine if the numbers are valid
valid_operators = "+-/*"    # Which operators are allowed to be used
operator_is_valid = None    # To check if the input operator is valid
end_result = 0  # Display the end result of the operation

while calculator_active:
    
    # Loop to input and verify the two first numbers
    # Also switch commas for dots to change numbers to float
    while numbers_are_valid == None:
        number_1 = input("Type first value: ")
        number_2 = input("Type second value: ")
        try:
            number_1 = number_1.replace(",", ".")
            number_2 = number_2.replace(",", ".")
            
            number_1 = float(number_1)
            number_2 = float(number_2)
            numbers_are_valid = True
            print("Both numbers are valid!")
        except:
            print("One or both numbers typed are not valid. Please try again!")
            
    # Operator validation. Doesn't allow for division by 0
    while operator_is_valid == None:
        operador = input("Type one of the for operators (+-/*): ")
        
        if operador not in valid_operators or len(operador) != 1:
            print("You didn't input a valid operator. Try again.")
        else:
            if operador == "/" and number_2 == 0:
                print("You cannot divide by 0! Try again!")
                numbers_are_valid = None
                operator_is_valid = None
                break
            else:
                print("You inserted a valid operator!")
                operator_is_valid = True
                
    # Doing the math
    if numbers_are_valid == True and operator_is_valid == True:
        end_result = eval(f"{number_1} {operador} {number_2}")
        print("The result of your operation is", end_result)
    else:
        pass
    
    # Leave or use the calculator again
    leave_software = input("Would you like to leave the application? Type [l] to leave: ").lower()
    if leave_software == "l":
        print("You ended the software.")
        calculator_active = False
        leave_software = ""
        break
    else:
        numbers_are_valid = None
        operator_is_valid = None
        end_result = 0
        os.system("cls")