# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        temp=list1
        while temp!=None:
            l.append(temp.val)
            temp=temp.next
        temp=list2
        while temp!=None:
            l.append(temp.val)
            temp=temp.next
        l.sort() 
        dummy=ListNode()
        temp=dummy
        for value in l:
            temp.next=ListNode(value)
            temp=temp.next
        return dummy.next           
        