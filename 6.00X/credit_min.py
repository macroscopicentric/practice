balance = 4213
annualInterestRate = .2
monthlyPaymentRate = .04

def pay_min(a, b, c):
	global balance
	month = 0
	total_paid = 0
	while month < 12:
		month += 1
		payment = monthlyPaymentRate * balance
		total_paid += payment
		balance = (balance - payment) + ((annualInterestRate / 12) * (balance - payment))
		print "Month: ", month
		print "Minimum monthly payment: ", round(payment, 2)
		print "Remaining balance: ", round(balance, 2)
	print "Total paid: ", round(total_paid, 2)
	print "Remaining balance: ", round(balance, 2)

pay_min(balance, annualInterestRate, monthlyPaymentRate)