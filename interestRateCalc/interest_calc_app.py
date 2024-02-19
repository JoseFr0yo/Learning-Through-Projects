# collect: principal, apr, years
# calculate monthly payment
# display monthly payment

def monthly_calc():
    print("Welcome to the Interest Rate Calculator App \n")

    principal = float(input("What is the initial amount of the loan: "))
    apr = float(input("What is the annual interest rate of the loan: "))
    years = int(input("What is the duration of the loan in years: "))

    monthly_interest_rate = apr / 12 / 100
    num_months = years * 12
    monthly_payment = principal * monthly_interest_rate / \
        (1 - (1 + monthly_interest_rate) ** -num_months)

    print(f"\nFor a loan of ${principal} at an annual interest rate of {apr}% for {
          years} years, you will have to pay ${monthly_payment:.2f} per month.")


monthly_calc()
