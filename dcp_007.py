# =-=-=-= DAY 7 [Medium] =-=-=-=
#
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
# number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as 'aaa',
# 'ka', and 'ak'.
#
# You can assume that the messages are decodable. For example, '001' is not
# allowed.


def decode_msg(msg_list):
    if len(msg_list) <= 1:
        return 1
    if int(''.join(msg_list[0:2])) <= 26:
        return decode_msg(msg_list[1:]) + decode_msg(msg_list[2:])
    return decode_msg(msg_list[1:])


print(decode_msg('111'))

# Googled this one, I just couldn't figure out a solution...
# Recursive solution makes sense though, first it checks if
# the list passed is only 1 long, and if it is it returns 1
# otherwise, it checks to see if the first two elements add
# to less than 26. If they do, it adds together two recursive
# calls with lists that start 1 over and 2 over. If they don't,
# the function is only called with a list that starts 1 over.
# does this over and over until total is calculated.
