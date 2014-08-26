def countdown():
	i = 0
	numbers = []
	
	input = int(raw_input("List end: "))
	
	while i < input + 1:
		print "At the top i is %d." % i
		numbers.append(i)
	
		increment = int(raw_input("Increment Value: "))
				
		i += increment		
		print "Numbers now: ", numbers
		print "At the bottom i is %d." % i
	
	print "The numbers: "

	for num in numbers:
		print num
	
countdown()