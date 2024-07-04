# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head):

        a =  head.next
        b = head.next
        sum=0
        while a:
            if a.val!=0: 
                sum+=a.val
            else:
                b.val=sum
                b.next=a.next
                b=b.next
                sum=0
            a=a.next
        return head.next