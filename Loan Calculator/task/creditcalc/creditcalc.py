import math
import sys

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
    overpayment = annuity * no_payments - principal
    print("Overpayment =", str(overpayment))


def calculate_ordinary_annuity(principal, interest, no_payments):  # interest: nominal (monthly) interest rate
    i = interest / (12 * 100)
    # print(str(principal), str(interest), str(no_payments))
    annuity = principal * i * math.pow(1 + i, no_payments) / (
            math.pow(1 + i, no_payments) - 1)
    rounded_annuity = math.ceil(annuity)
    print("Your monthly payment = {}!".format(str(rounded_annuity)))


def calculate_differentiated_payment(principal, interest, no_payments):
    i = interest / (12 * 100)
    sum_payment = 0
    for month in range(1, no_payments + 1):
        payment = principal / no_payments + i * (principal - ((principal * (month - 1)) / no_payments))
        payment_int = math.ceil(payment)
        sum_payment += payment_int
        print("Month {}: payment is {}".format(str(month), str(payment_int)))
    overpayment = sum_payment - principal
    print()
    print("Overpayment =", str(overpayment))


def calculate_loan_principal(annuity, interest, no_payments):
    i = interest / (12 * 100)
    principal = annuity / (i * (math.pow(1 + i, no_payments)) / (
            math.pow(1 + i, no_payments) - 1))
    print("Your loan principal = {}!".format(math.floor(principal)))
    overpayment = annuity * no_payments - principal
    print("Overpayment =", str(principal))


def console_input_variant():
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


def throw_parameter_error():
    print("Incorrect parameters")
    exit()


def interpret_command_argument(arguments):
    payment_type = None
    payment = None
    principal = None
    periods = None
    interest = None
    # print(arguments)
    for argument in arguments[1:]:
        if not argument[0:2] == "--" or len(arguments) < 4:
            throw_parameter_error()
        variable, value = argument.lstrip("--").split("=")
        if variable == "type":
            payment_type = value
        elif variable == "payment":
            payment = float(value)
        elif variable == "principal":
            principal = float(value)
        elif variable == "periods":
            periods = int(value)
        elif variable == "interest":
            interest = float(value)
    if (payment_type not in ["annuity", "diff"]) or \
            (payment_type == "diff" and payment is not None) or \
            interest is None or \
            (payment and payment < 0) or (principal and principal < 0) \
            or (periods and periods < 0) or (interest and interest < 0):
        throw_parameter_error()
    else:
        if payment_type == "diff":
            calculate_differentiated_payment(principal, interest, periods)
        elif payment_type == "annuity":
            if principal and interest and periods and not payment:
                calculate_ordinary_annuity(principal, interest, periods)
            elif principal and interest and payment and not periods:
                calculate_number_of_payments(payment, interest, principal)
            elif periods and payment and interest and not principal:
                calculate_loan_principal(payment, interest, periods)
            else:
                throw_parameter_error()


args = sys.argv
if args == 1:
    console_input_variant()
else:
    interpret_command_argument(args)
