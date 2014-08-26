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

def find_path(root):
    if root == None:
        return []
    elif root.r < a:
        return find_path(root.r)
    elif root > b:
        return []
    elif root == a:
        tree = [root] + find_path(root.r)
        if b in tree:
            return tree
        else:
            return [root]
    elif root == b:
        return [root]
    else:
        return find_path(root.l) + [root] + find_path(root.r)