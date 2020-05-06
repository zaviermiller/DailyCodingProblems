# =-=-=-= DAY 8 [Easy] =-=-=-=
#
# A unival tree (which stands for "universal value") is a tree where all nodes
# under it have the same value.
#
# Given the root to a binary tree, count the number of unival subtrees.
#
# For example, the following tree has 5 unival subtrees:
#
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def children(self):
        return f"{self.left}, {self.right}"

    def __repr__(self):
        return str(self.val)


def count_uvs(node):
    if node.left is None and node.right is None:
        return 1
    if node.left.val == node.right.val and node.right.val == node.val:
        return 1 + count_uvs(node.left) + count_uvs(node.right)
    return count_uvs(node.left) + count_uvs(node.right)


node = Node(1, Node(1, Node(1, Node(1), Node(1)), Node(0)), Node(0))
print(count_uvs(node))
