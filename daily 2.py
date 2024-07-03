import math
def minDifference(nums):
    """

    :type nums: object
    """
    if len(nums) < 4:
        min_diff = 0
        for i in range(len(nums)):
            nums[i]= nums[0]
    else:
        diffs = []
        for i in range(4):
            a = sorted(nums, reverse = True)[i]
            b = sorted(nums)[3-i]
            diffs.append(abs(a-b))
        k = i
        min_diff = diffs[0]
        for i,diff in enumerate(diffs):
            if min_diff >= diff:
                min_diff = diff
                j = i
        for i in range (j+1):
            nums[nums.index(sorted(nums, reverse = True)[0])] = nums[nums.index(sorted(nums, reverse = True)[j])]
        for i in range (4-j):
            nums[nums.index(sorted(nums)[0])] = nums[nums.index(sorted(nums)[3-j])]
    print (min_diff)
    print (nums)

minDifference([1,11,15,17])
