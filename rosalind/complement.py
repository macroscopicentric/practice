string = "AAAACCCGGT"
new_string = ""

for i in string:
	if i == 'T':
		new_string += "A"
	elif i == 'A':
		new_string += "T"
	elif i == 'C':
		new_string += "G"
	elif i == 'G':
		new_string += "C"

new_string = new_string[::-1]
print new_string