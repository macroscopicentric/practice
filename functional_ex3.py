def zero(s):
    if s[0] == "0":
        return s[1:]

def one(s):
    if s[0] == "1":
        return s[1:]

#Imperative:
# def rule_sequence(s, rules):
#     for rule in rules:
#         s = rule(s)
#         if s == None:
#             break

#     return s

#Declarative, aka recursive:
# def rule_sequence(s, rules):
#     if rules[0](s) == None:
#         return None
#     elif len(rules) == 1:
#         return rules[0](s)
#     else:
#         return rule_sequence(rules[0](s), rules[1:])

#Mary's solution:
def rule_sequence(s, rules):
    if s == None or not rules:
        return s
    else:
        return rule_sequence(rules[0](s), rules[1:])

print rule_sequence('0101', [zero, one, zero])
# => 1

print rule_sequence('0101', [zero, zero])
# => None