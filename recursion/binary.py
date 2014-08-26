class Node(object):

    def __init__(self, value, l=None, r=None):

        self.value = value
        self.left = l
        self.right = r

tree1 = Node(1, 
             Node(2,
                  Node(3),
                  Node(4)),
             Node(5,
                  Node(6),
                  Node(7)))

tree2 = Node(1,
             Node(2, 
                  Node(3)),
             Node(4))

def sum_tree(tree):
    if tree == None:
        return 0
    else:
        return tree.value + sum_tree(tree.left) + sum_tree(tree.right)

def print_tree(tree):
    if tree == None:
        return ''
    else:
        return "%s%s%s" % (str(tree.value) + ' ', print_tree(tree.left), print_tree(tree.right))

print print_tree(tree1)
print print_tree(tree2)

print sum_tree(tree1)
print sum_tree(tree2)

# lastIndexOf x [] = -1
# lastIndexOf x (x:xs) = either 0 or (1 + lastIndexOf x xs)
# lastIndexOf x (y:xs) = 1 + lastIndexOf xs