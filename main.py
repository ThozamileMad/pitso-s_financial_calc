import math


def catch_value_error(question):
    try:
        value = float(question)
        return [value, True]
    except ValueError:
        print("Error! Invalid input, please enter a number.")
        return False

        
def calculate_bond():
    # The function catch_value_error produces an error if the input entered is invalid
    
    house_value_valid = catch_value_error(input("Please enter the current value of the house: "))
    if house_value_valid[1]:
        house_value = house_value_valid[0]
    else:
        house_value_valid = catch_value_error(input("Please enter the current value of the house: "))

    rate = float(input("Please enter the current annual interest rate : "))

    # converts the annual interest into monthly interest
    rate = rate / float(12)

    duration = float(input("how many months do you plan on paying your bond"))

    # calculates the bond repayment
    Bond_repayment = (rate * house_value) / (1 - (1 + rate) ** (-duration))
    Bond_repayment = round(Bond_repayment, 2)

    print(f'your bond repayment is R{Bond_repayment}')


def calculate_interest():
    initial_investment = float(input("how much would like to invest : "))
    rate = input("what rate would like to receive")
    rate = float(rate)/float(100)
    duration = float(input("how long would like to invest"))
    type_of_interest = input("choose your preferred interest : ").lower()

    if type_of_interest == 'compound':
        roi = (initial_investment * math.pow((float(1) + rate), (duration)))
        roi = round(roi, 2)
        print(f'your return on investment is R{roi}')
    elif type_of_interest == 'simple':
        roi = (initial_investment * (float(1 + rate * duration)))
        roi = round(roi, 2)
        print(f'your return on investment is R{roi}')

# the program is used to calculate the bond or investments of an individual
# first it asks them to enter what they would like to do
print("what would you like to do today. \ninvestment(calculate potential interest on an investment) or \nbond(calculate your home loan repayments) ")
# it converts their output to lowercases so it can recognise the input in every key entered
choice = input("choose bond or investment : ").lower().strip()
is_invalid = False
if choice not in ["bond", "investment"]:
    is_invalid = True

while is_invalid:
    print("Error!!! Invalid input, please enter the following values: bond or investment.")
    choice = input("choose bond or investment : ").lower()
    if choice == "bond" or choice == "investment":
        is_invalid = False

if choice == "bond":
    calculate_bond()
else:
    calculate_interest()
