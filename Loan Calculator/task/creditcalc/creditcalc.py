import math

# loan_principal = 'Loan principal: 1000'
# final_output = 'The loan has been repaid!'
# first_month = 'Month 1: repaid 250'
# second_month = 'Month 2: repaid 250'
# third_month = 'Month 3: repaid 500'
#
# # write your code here
# print(loan_principal)
# print(first_month)
# print(second_month)
# print(third_month)
# print(final_output)


def ask_for_monthly_payments():
    payments = int(input("Enter the monthly payment: >"))
    return payments


def ask_for_number_of_months():
    no_of_months = int(input("Enter the number of month: >"))
    return no_of_months


def calculate_monthly_payment(principal, no_of_month):
    payment = math.ceil(principal / no_of_month)
    overflow = payment * no_of_month - principal
    last_payment = payment - overflow
    print()
    print("Your monthly payment = {} and the last payment = {}.".format(str(payment), str(last_payment)))


def calculate_number_of_payments(principal, payments):
    no_of_payments = math.ceil(principal / payments)
    print()
    print("It will take {} month{} to repay the loan".format(str(no_of_payments), "s" if no_of_payments > 1 else ""))


input_principal = int(input("Enter the loan principal: >"))
user_choice = input('''What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:''')

if user_choice == "p":
    number_of_months = ask_for_number_of_months()
    calculate_monthly_payment(input_principal, number_of_months)
elif user_choice == "m":
    monthly_payment = ask_for_monthly_payments()
    calculate_number_of_payments(input_principal, monthly_payment)
