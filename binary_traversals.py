class Node(object):
    def __init__(self, data, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left
# Pre-order traversal
# Pre-order traversal
def pre_order(node):
    lst = []
    if node is None:
        return []
    lst.append(node.data)
    return lst + pre_order(node.left) + pre_order(node.right)

# In-order traversal
def in_order(node):
    lst = []
    if node is None:
        return []
    lst.append(node.data)
    return in_order(node.left) + lst + in_order(node.right)

# Post-order traversal
def post_order(node):
    lst = []
    if node is None:
        return []
    lst.append(node.data)
    return post_order(node.left) + post_order(node.right) + lst
