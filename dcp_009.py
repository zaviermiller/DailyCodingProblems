# =-=-=-= DAY 9 [Hard] =-=-=-=
#
# Given a list of integers, write a function that returns the largest sum of
# non-adjacent numbers. Numbers can be 0 or negative.
# 
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1,
# 1, 5] should return 10, since we pick 5 and 5.
# 
# Follow-up: Can you do this in O(N) time and constant space?

def largest_na_sum(nums):
    queue = []
    queue.append((0,0))

    totals = []

    while queue:      
        s = queue.pop(0)
        i, prev = s
        prev += nums[i]
        if i + 2 < len(nums):
            for j in range(i + 2, len(nums)):
                queue.append((j,prev))
        else:
            totals.append(prev)
    
    return max(totals)


print(largest_na_sum([5,1,1,5]))
