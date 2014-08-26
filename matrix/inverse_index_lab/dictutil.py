## Task 2
def dict2list(dct, keylist):
    L = [dct[i] for i in keylist]
    return L

def list2dict(L, keylist):
    dictionary = {keylist[i]: L[i] for i in range(0, len(L))}
    return dictionary

## Task 3
def listrange2dict(L):
    """
    Input: a list
    Output: a dictionary that, for i = 0, 1, 2, . . . , len(L), maps i to L[i]

    You can use list2dict or write this from scratch
    """
    dictionary = {i: L[i] for i in range(0, len[L])}
    return dictionary

dictionary = {'a':'A', 'b':'B', 'c':'C'}
klist = ['b','c','a']
llist = ['B','C','A']

print dict2list(dictionary, klist)
print list2dict(llist, klist)