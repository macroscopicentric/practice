file = open("rosalind_ini5.txt", "r")

num_lines = sum(1 for line in file)
# print num_lines

file.seek(0)
line_list = file.readlines()

file.close()

# print line_list

for i in range(0, (num_lines + 1)):
	if i % 2 == 0:
		print line_list[i + 1],