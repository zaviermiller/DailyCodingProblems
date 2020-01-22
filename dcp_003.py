# =-=-=-= DAY 3 [Medium] =-=-=-=
#
# Given the root to a binary tree, implement serialize(root), which serializes the
# tree into a string, and deserialize(s), which deserializes the string back into
# the tree.
#
# For example, given the following Node class
#
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# The following test should pass:
#
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'
import json


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    s_tree = '"' + node.val + '"'
    s_tree += ((': [' + serialize(node.left) + ', ') if node.left is not None else ': [null,') + \
        ((serialize(node.right) + ']')
         if node.right is not None else 'null]')
    return '{' + s_tree + '}'


def deserialize(s):
    tree_dict = (json.loads(s)) if isinstance(s, str) else s
    try:
        for i in tree_dict:
            children = []
            for item in tree_dict[i]:
                children.append(deserialize(item))
            node = Node(i, children[0], children[1])
            return node

    except:
        return None


node = Node('root', Node('left', Node('left.left')), Node('right'))
print(deserialize(serialize(node)).left.left.val == 'left.left')

# Did pretty well, knew how to solve serialize problem pretty quickly.
# I decided to use JSON as the serial legend, as this is one of the
# most popular ways to pass data in web apps.
# The deserialize method was pretty difficult, it took me a while,
# but once I started trying to solve the problem with theoretical
# recursive logic rather than trying to trace the code, the task
# became immensely easier.
#
# ====| ANALYSIS |====
#
# serialize(node): O(N)
# deserialize(s): O(2N^2) - not sure
