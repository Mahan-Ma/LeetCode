nums1 =[0,1,1,2,2,0,0,0]
m =5
nums2 =[0,3,3]
n =3
class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp1 = []
        for item in nums1:
            if item != 0:
                temp1.append(item)
        temp2 = []
        for item in nums2:
            if item != 0:
                temp2.append(item)
        i = 0
        itemBool = False
        rem1 = []
        rem2 = []
        for item in temp1:
            if temp2:
                for sec_item in temp2:
                    if item < sec_item:
                        nums1[i] = item
                        rem1.append(item)
                        i += 1
                        print (i, "1")
                        #itemBool = False
                        break
                    elif item == sec_item:
                        nums1[i] = item
                        rem1.append(item)
                        nums1[i+1] = sec_item
                        rem2.append(sec_item)
                        i += 2
                        #itemBool = False
                        break
                    else:
                        nums1[i] = sec_item
                        rem2.append(sec_item)
                        itemBool = True
                        i += 1
                for remove_item in rem2:
                    if(remove_item):temp2.remove(remove_item)
            # else:
            #     nums1[i] = item
            #     rem1.append(item)
            #     i += 1
            rem2 = []
        for remove_item in rem1:
            if(remove_item):temp1.remove(remove_item)

        # if (itemBool):
        for item in temp1:
            nums1[i] = item
            i+=1

        for item in temp2:
            nums1[i] = item
            i+=1
        positive_num = False
        zero_index = None
        if len(nums1)> i:
            num_zeros = len(nums1)-i
            for i,item in enumerate(nums1):
                if item <0:
                    continue
                else:
                    positive_num = True
                    zero_index = i
                    break
                break
            if positive_num:
                i = len(nums1)
                if zero_index != None:
                    while i > zero_index + num_zeros:
                        nums1[i-1] = nums1[i-1-num_zeros]
                        i -=1
                    for i in range(zero_index, zero_index+num_zeros):
                        nums1[i] = 0


        return nums1
a = Solution()
print (a.merge(nums1,m,nums2,n))
