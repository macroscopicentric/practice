string = "GATGGAACTTGACTACGTAAATT"

string = [s.replace("T", "U") for s in string]
string = ''.join(string)

print string