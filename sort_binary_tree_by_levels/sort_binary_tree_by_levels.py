class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(top_node):
    def _walk_values(top):
        yield top.value
        next_level = [child for child in (top.left, top.right) if isinstance(child, Node)]
        while next_level:
            current_level = next_level
            next_level = []
            for node in current_level:
                yield node.value
                next_level.extend([child for child in (node.left, node.right) if isinstance(child, Node)])

    return list(_walk_values(top_node)) if isinstance(top_node, Node) else []