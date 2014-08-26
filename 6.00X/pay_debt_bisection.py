balance = 320000
annualInterestRate = .2

def pay_min(a, b):
    test_balance = balance
    month = 0
    monthly_interest_rate = annualInterestRate / 12
    lower = balance / 12.0
    upper = (balance * (1 + monthly_interest_rate)**12) / 12.0
    payment = (upper + lower) / 2
    while test_balance > .001 or test_balance < -.001:
        month = 0
        test_balance = balance
        while month < 12:
            month += 1
            test_balance = (test_balance - payment) + ((monthly_interest_rate) * (test_balance - payment))
        if test_balance > 0:
            lower = payment
            payment = (upper + lower) / 2
        else:
            upper = payment
            payment = (upper + lower) / 2
    print "Lowest payment: ", round(payment, 2)

pay_min(balance, annualInterestRate)