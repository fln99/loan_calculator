# Loan Calculator from Jetbrains Academy

---

With this calculator you'll be able to calculate:

* Annuity payment

* Differentiate payment

This a developer version, however you may know how to run a python program on the terminal.

On the terminal you can use theses parameters:

**_Note: this calculator require 4 parameters on the terminal._**

**--type=** (annuity or differentiate);

**--payment=** monthly payment amount;

**--principal=** (it's the principal loan) used in both types. If you know the interest, annuity payment and number of months, you can calculate the principal loan;

**--periods=** number of months needed to repay the loan;

**--interest=** It's the interest rate, may specified without percent sign.

---

##### Below you have some examples of calculus:

The **overpayment** is the difference the sum of the payments and the loan principal.

*Follow this examples to apply by yourself :)*

Calculating the payment of each month in the period:

```
> python creditcalc.py --principal=1000000 --periods=10 --interest=10
Month 1: payment is 108334
Month 2: payment is 107500
Month 3: payment is 106667
Month 4: payment is 105834
Month 5: payment is 105000
Month 6: payment is 104167
Month 7: payment is 103334
Month 8: payment is 102500
Month 9: payment is 101667
Month 10: payment is 100834

Overpayment = 45837
```

Calculating annuity payment:

```
> python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
Your annuity payment = 21248!

Overpayment = 274880
```

Calculating loan principal:

```
> python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
Your loan principal = 800018!

Overpayment = 246622
```

Calculating how long it will take to make the repay:

```
> python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
It will take 2 years to repay this loan!

Overpayment = 52000
```

---

Access the Jetbrain Academy by [this link](hyperskill.org). Signup and become a Python Developer!
