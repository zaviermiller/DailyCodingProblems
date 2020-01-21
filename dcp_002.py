# =-=-=-= DAY 2 [Hard] =-=-=-=
#
# Given an array of integers, return a new array such that each element at index i
# of the new array is the product of all the numbers in the original array except
# the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be
# [2, 3, 6].
#
# Follow-up: what if you can't use division?

from functools import reduce


def weirdify_array(arr):
    new_arr = []
    total = reduce(lambda x, y: x * y, arr)

    for i in arr:
        new_arr.append(int(total / i))
    return new_arr


def weirdify_array_no_division(arr):
    new_arr = []

    for i in arr:
        value = 1
        for j in arr:
            if j != i:
                value *= j
        new_arr.append(int(value))
    return new_arr


print(weirdify_array_no_division([1, 2, 3, 4, 5]))

# This one was better, didn't have to Google exact solution.
# I did however need to Google the reduce function to get the mult total.
# I think I got the best time for no div possible but I dont know. It is O(N^2)
# as it needs to loop through the array N times for each pass.
# The division allowed one is O(2N) which makes it as efficient as possible (linear)
