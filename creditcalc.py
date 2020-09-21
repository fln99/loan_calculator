import sys
import math
from calculator_resources.resources import time_to_repay, calc_nominal_interest, calc_principal_loan, calc_monthly, calc_annuity, calc_time

if len(sys.argv) != 5 or sys.argv[1] != '--type=diff' and sys.argv[1] != '--type=annuity':
    print("Incorrect parameters")

else:
    if '--type=diff' in sys.argv[1]:
        if '--principal=' in sys.argv[2] and '--periods=' in sys.argv[3] and '--interest=' in sys.argv[4]:
            principal = float(sys.argv[2][12:])
            periods = int(sys.argv[3][10:])
            interest = float(sys.argv[4][11:])

            calc_monthly(principal, periods, interest)
        else:
            print("Incorrect parameters")

    elif '--type=annuity' in sys.argv[1]:
        if '--payment=' in sys.argv[2] and '--periods=' in sys.argv[3] and '--interest=' in sys.argv[4]:
            payment = float(sys.argv[2][10:])
            periods = float(sys.argv[3][10:])
            interest = float(sys.argv[4][11:])

            calc_principal_loan(payment, periods, interest)
        
        elif '--principal=' in sys.argv[2] and '--payment=' in sys.argv[3] and '--interest=' in sys.argv[4]:
            principal = float(sys.argv[2][12:])
            payment = float(sys.argv[3][10:])
            interest = float(sys.argv[4][11:])

            calc_time(principal, payment, interest)

        elif '--principal=' in sys.argv[2] and '--periods=' in sys.argv[3] and '--interest=' in sys.argv[4]:
            principal = float(sys.argv[2][12:])
            periods = float(sys.argv[3][10:])
            interest = float(sys.argv[4][11:])

            calc_annuity(principal, periods, interest)
        else:
            print("Incorrect parameters")