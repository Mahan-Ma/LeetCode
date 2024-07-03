class Solution:
    def removeDuplicates(nums):
        if len(nums)>1:
            for i in range(len(nums)-1,-1,-1):
                if(nums[i] == nums[i-1]):
                    nums.pop(i)
                    if(i==1):
                        break
        k = len(nums)
        return k
a= Solution
print(a.removeDuplicates(nums=[1,1,1]))