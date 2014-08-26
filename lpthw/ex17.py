from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read()
#indata = in_file.read()

outdata = open(to_file, "w").write(indata)
#out_file.write(indata)

#Still getting an error. Why? For both outdata and indata: AttributeError 'str'
#or None class has no attribute "close."

#From the site: Python closes the file after indata = open(from_file).read() runs.
#No need to file.close()

#Tip from ex17: cat filename in Terminal prints entire file to Terminal's screen.