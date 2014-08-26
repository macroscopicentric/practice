from sys import argv
#imports command "argv" from the sys library/module

script, filename = argv
#argv has two arguments in this program

txt = open(filename)
#creates a variable named "txt" that has all the info from your file "filename"
#"filename" collects whatever you asked it to open in the command line arguments

print "Here's your file %r:" % filename
#print text with the "filename" (verification)
print txt.read()
#prints the variable "txt"
#why do I need both txt.read() AND open()?

#print "Type the filename again:"
#file_again = raw_input("> ")
#creates a second variable named "file_again" that takes raw input (
#assumption: valid file name)

#txt_again = open(file_again)

#print txt_again.read()