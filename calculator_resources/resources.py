import math

def time_to_repay(year, month):
    """Shows the time spent to repay the loan.

    Keyword argument:
    year -- year to repay
    month -- month to repay
    """
    if month >= 12:
        year += month // 12
        month = month % 12
    
    month_word = "months" if month > 1 else "month"

    year_word = "years" if year > 1 else "year"

    if month == 0:
        print(f"This will take {year} {year_word} to repay this loan!")
    elif year == 0:
        print(f"This will take {month} {month_word} to repay this loan!")
    else:
        print(f"This will take {year} {year_word} and {month} {month_word} to repay this loan!")


def calc_nominal_interest(val):
    """Simple calc of the nominal interest by 1 year.

    val -- the percentual interest
    """
    return val / (12 * 100)


def calc_principal_loan(pay, per, intr):
    """Shows the user's loan principal and overpayment.

    pay -- monthly payment amount
    per -- number of months needed to repay the loan
    intr -- interest rate without conversion to nominal interest
    """
    intr = calc_nominal_interest(intr)
    loan_principal = pay / (intr * (1 + intr) ** per / ((1 + intr) ** per - 1))

    print(f"Your loan principal = {math.floor(loan_principal)}!")
    print(f"Overpayment = {math.ceil((pay * per) - loan_principal)}")


def calc_monthly(loan, per, intr):
    """Print every month and the respective payment and the overpayment.

    loan -- principal loan
    per -- number of months needed to repay the loan
    intr -- interest rate without conversion to nominal interest 
    """
    month = 1
    intr = calc_nominal_interest(intr)
    overpayment = 0

    for _ in range(per):
        formula = (loan / per) + intr * (loan - loan * (month - 1) / per)

        print(f"Month {month}: payment is {math.ceil(formula)}")

        overpayment += math.ceil(formula)
        month += 1

    print()
    print(f"Overpayment = {round(overpayment - loan)}")


def calc_annuity(loan, per, intr):
    """Total of the payment on the final of 1 year and shows the overpayment.

    loan -- principal loan 
    per -- number of months needed to repay the loan
    intr -- interest rate without conversion to nominal interest
    """
    intr = calc_nominal_interest(intr)
    monthly_payment = (intr * (1 + intr) ** per / ((1 + intr) ** per - 1) * loan)

    print(f"Your annuity payment {math.ceil(monthly_payment)}!")
    print(f"Overpayment = {round(math.ceil(monthly_payment) * per - loan)}")


def calc_time(loan, mth, intr):
    """The total of time to repay the loan and the overpayment.

    loan -- principal loan
    mth -- monthly payment
    intr -- interest rate without conversion to nominal interest
    """
    intr = calc_nominal_interest(intr)
    number_of_payments = math.log(mth / (mth - intr * loan), (1 + intr))
    
    year = math.ceil(number_of_payments // 12)
    month = math.ceil(number_of_payments % 12)

    time_to_repay(year, month)

    print(f"Overpayment = {round(mth * math.ceil(number_of_payments) - loan)}")