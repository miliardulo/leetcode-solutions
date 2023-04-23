# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list1 or list2):
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        if list1.val>list2.val:
            list1,list2 = list2,list1
        curr: Optional[ListNode] = list1
        while list2:
            if not curr.next or list2.val<curr.next.val:
                curr.next = ListNode(list2.val, curr.next)
                list2=list2.next
                continue
            curr=curr.next
        return list1