class Solution:
    def intersect(self, nums1, nums2) :
        intersect_arr = []
        rem2 = None
        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2:
                    intersect_arr.append(num1)
                    rem2 = num2
                    break
            if rem2:
                nums2.remove(rem2)
                rem2 = None
        return intersect_arr


nums1 =[1,2,2,1]
nums2 =[2]

a = Solution
a.intersect(None, nums1,nums2)

