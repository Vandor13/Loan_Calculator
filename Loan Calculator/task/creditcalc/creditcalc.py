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
from typing import Any, Union


def ask_for_monthly_payments():
    payments = int(input("Enter the monthly payment: > "))
    return payments


def ask_for_number_of_months():
    no_of_months = int(input("Enter the number of month: > "))
    return no_of_months


def get_no_payment_arguments():
    principal = float(input("Enter the loan principal: > "))
    payment = float(input("Enter the monthly payment: > "))
    interest = float(input("Enter the loan interest: > "))
    return principal, payment, interest


def get_payment_amount_arguments():
    principal = float(input("Enter the loan principal: > "))
    no_payments = float(input("Enter the number of periods: > "))
    interest = float(input("Enter the loan interest: > "))
    return principal, no_payments, interest


def get_principal_arguments():
    annuity = float(input("Enter the annuity payment: > "))
    no_payments = float(input("Enter the number of periods: > "))
    interest = float(input("Enter the loan interest: > "))
    return annuity, no_payments, interest


def calculate_monthly_payment(principal, no_of_month):
    payment = math.ceil(principal / no_of_month)
    overflow = payment * no_of_month - principal
    last_payment = payment - overflow
    print()
    print("Your monthly payment = {} and the last payment = {}.".format(str(payment), str(last_payment)))


def calculate_simple_number_of_payments(principal, payments):
    no_of_payments = math.ceil(principal / payments)
    print()
    print("It will take {} month{} to repay the loan".format(str(no_of_payments), "s" if no_of_payments > 1 else ""))


def calculate_number_of_payments(annuity, interest, principal):
    i = interest / (12 * 100)
    x = annuity / (annuity - i * principal)
    base = float(i + 1)
    no_payments = math.ceil(math.log(x, base))
    time_string = ""
    if no_payments >= 12:
        years = no_payments // 12
        time_string = "{} year".format(years)
        if years > 1:
            time_string += "s"
    months = no_payments % 12
    if months != 0:
        if time_string != "":
            time_string += " and "
        time_string += "{} month".format(months)
        if months > 1:
            time_string += "s"
    print("It will take", time_string, "to repay this loan!")


def calculate_ordinary_annuity(principal, interest, no_payments):  # interest: nominal (monthly) interest rate
    i = interest / (12 * 100)
    annuity: Union[float, Any] = principal * i * math.pow(1 + i, no_payments) / (
                math.pow(1 + i, no_payments) - 1)
    rounded_annuity = math.ceil(annuity)
    print("Your monthly payment = {}!".format(str(rounded_annuity)))


def calculate_loan_principal(annuity, interest, no_payments):
    i = interest / (12 * 100)
    principal = annuity / (i * (math.pow(1 + i, no_payments)) / (
                math.pow(1 + i, no_payments) - 1))
    print("Your loan principal = {}!".format(math.floor(principal)))


user_choice = input('''What do you want to calculate?
type "n" - for number of monthly payments,
type "a" - for annuity monthly payment amount,
type "p" for loan principal:\n''')

if user_choice == "n":
    user_principal, user_payment, user_interest = get_no_payment_arguments()
    calculate_number_of_payments(user_payment, user_interest, user_principal)
elif user_choice == "a":
    user_principal, user_no_payment, user_interest = get_no_payment_arguments()
    calculate_ordinary_annuity(user_principal, user_interest, user_no_payment)
elif user_choice == "p":
    user_annuity, user_no_payments, user_interest = get_principal_arguments()
    calculate_loan_principal(user_annuity, user_interest, user_no_payments)
