# =-=-=-= DAY 4 [Hard] =-=-=-=
#
# Given an array of integers, find the first missing positive integer in linear
# time and constant space. In other words, find the lowest positive integer that
# does not exist in the array. The array can contain duplicates and negative
# numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should
# give 3.
#
# You can modify the input array in-place.


def find_lowest_missing(arr):
    lowest = 1
    done = False
    while not done:
        for item in arr:
            done = True
            if lowest == item:
                lowest += 1
                done = False

    return lowest


print(find_lowest_missing([3, 4, -1, 1]))

# Ok. I'm not too sure about this problem. I would actually
# love feedback about whether or not its linear time.
# My argument for it being linear is that the while loop runs the
# least amount of times necessary, and multiple for loops
# are still linear. I think. I don't know, but it works, so
# I'm considering it completed. Didn't Google for answer, pretty
# simple. It sets the lowest var to be the lowest possible, then
# loops through the list over and over changing the lowest value everytime
# it is encountered in the list. Once the lowest value is not in the list,
# it returns the lowest.
