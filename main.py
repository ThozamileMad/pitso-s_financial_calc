import math


def catch_value_error(question):
    invalid = False
    try:
        value = float(input(question))
        return value
    except ValueError:
        print("\nError! Invalid input, please enter a number.")
        invalid = True

    if invalid:
        return catch_value_error(question)
        

def calculate_bond():
    # The function catch_value_error produces an error if the input entered is invalid but returns the user's input if the value is valid
    house_value = catch_value_error("Please enter the current value of the house: ")
 
    rate = catch_value_error("Please enter the current annual interest rate : ")

    # converts the annual interest into monthly interest
    rate = rate / float(12)

    duration = catch_value_error("How many months do you plan on paying your bond: ")

    # calculates the bond repayment
    Bond_repayment = (rate * house_value) / (1 - (1 + rate) ** (-duration))
    Bond_repayment = round(Bond_repayment, 2)
    print(f'Your bond repayment is R{Bond_repayment}')
    if input("\nDo you wish to restart the program?\nIf you do enter y.\nIf you do not then enter any key(except for y): ").lower() == "y":
        start_program()


def calculate_interest():
    initial_investment = catch_value_error("How much would like to invest : ")
    rate = catch_value_error("What rate would like to receive: ")/100
    duration = catch_value_error("How long would like to invest(in years): ")
    type_of_interest = choice_invalid_reproduce_question("Enter your preferred interest(simple or compound): ",
                                                         ["simple", "compound"],
                                                         "\nError!!! Invalid input, please enter the following values: simple or compound.")

    if type_of_interest == 'compound':
        roi = (initial_investment * math.pow((float(1) + rate), (duration)))
        roi = round(roi, 2)
        print(f'Your return on investment is R{roi}')
    elif type_of_interest == 'simple':
        roi = (initial_investment * (float(1 + rate * duration)))
        roi = round(roi, 2)
        print(f'Your return on investment is R{roi}')

    if input("\nDo you wish to restart the program?\nIf you do enter y.\nIf you do not then enter any key(except for y): ").lower() == "y":
        start_program()


def choice_invalid_reproduce_question(question, choices: list, error_message):
    choice = input(question).lower().strip()
    is_invalid = False
    if choice not in choices:
        is_invalid = True

    while is_invalid:
        print(error_message)
        choice = input(question).lower().strip()
        if choice == choices[0] or choice == choices[1]:
            is_invalid = False
    return choice


def start_program():
    print("\nWhat would you like to do today. \ninvestment(calculate potential interest on an investment) or \nbond(calculate your home loan repayments) ")
    choice = choice_invalid_reproduce_question("choose bond or investment : ",
                                               ["bond", "investment"],
                                               "\nError!!! Invalid input, please enter the following values: bond or investment.",
                                               )
    if choice == "bond":
        calculate_bond()
    else:
        calculate_interest()
            

# the program is used to calculate the bond or investments of an individual
start_program()      
