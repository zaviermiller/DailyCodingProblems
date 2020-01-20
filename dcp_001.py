# =-=-=-= DAY 1 =-=-=-=
#
# Given a list of numbers and a number k, return whether any two numbers from the
# list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?


def add_to(nums, k):
    set_nums = set()

    for num in (nums):
        if k - num in set_nums:
            return True
        set_nums.add(num)

    return False


print(add_to([10, 10, 3, 7], 20))

# Had to Google, but I understand the logic behind it.
# Loop through the list of numbers, and check if the target - current num is in set_nums
# If it is, return True, the two values have been found (if you want to know what it is, return k - num and num)
# If it isn't, add that number to the set_nums (seperate set, prevents false positives)
# At the end, if True isn't returned, return False
