#Unfunctional
names = ['Mary', 'Isla', 'Sam']

# for i in range(len(names)):
#     names[i] = hash(names[i])

# print names

#Functional
# secret_names = map(lambda x: hash(x), names)
#Duh, can just do:
secret_names = map(hash, names)
print secret_names