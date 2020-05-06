# =-=-=-= DAY 72 [Hard] =-=-=-=
#
# In a directed graph, each node is assigned an uppercase letter. We define a
# path's value as the number of most frequently-occurring letter along that path.
# For example, if a path in the graph goes through "ABACA", the value of the path
# is 3, since there are 3 occurrences of 'A' on the path.
# 
# Given a graph with n nodes and m directed edges, return the largest value path
# of the graph. If the largest value is infinite, then return null.
# 
# The graph is represented with a string and an edge list. The i-th character
# represents the uppercase letter of the i-th node. Each tuple in the edge list 
# (i, j) means there is a directed edge from the i-th node to the j-th node.
# Self-edges are possible, as well as multi-edges.
# 
# For example, the following input graph:
# 
# ABACA
