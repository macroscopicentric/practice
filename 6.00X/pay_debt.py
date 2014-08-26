balance = 3329
annualInterestRate = .2

def pay_min(a, b):
    test_balance = balance
    month = 0
    total_paid = 0
    payment = 0
    while test_balance > 0:
        payment += 10
        month = 0
        test_balance = balance
        while month < 12:
            month += 1
            test_balance = (test_balance - payment) + ((annualInterestRate / 12) * (test_balance - payment))
    print "Lowest payment: ", int(payment)

pay_min(balance, annualInterestRate)