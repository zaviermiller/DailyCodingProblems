# =-=-=-= DAY 5 [Medium] =-=-=-=
#
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and
# last element of that pair. For example, car(cons(3, 4)) returns 3, and
# cdr(cons(3, 4)) returns 4.
#
# Given this implementation of cons:
#
# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
#
# Implement car and cdr.


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    def f(x, y):
        return x
    return pair(f)


def cdr(pair):
    def f(x, y):
        return y
    return pair(f)


assert cdr(cons(3, 4)) == 4

# This one was weird. It was more of a
# Python what-do-you-know rather than a
# test of DS & A. It wasn't bad, I Googled
# the answer but I know a lot more now than
# I did!
