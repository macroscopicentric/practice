s = 'azcbobobegghakl'
count = 0
letters = "abcdefghijklmnopqrstuvwxyz"
alph_order = ""
alphabet = dict(zip(letters, range(1,27)))
# for i in range(0, len(s)):
# 	if count >= 26:
# 		print "done"
# 	elif alphabet[s[i:-1]] > count:
# 		alph_order += s[i]
# 		count = alphabet[s[i]]
# 		print alph_order
# 		print count
# 	else:
# 		print "error"
print alphabet[s[1:7]]