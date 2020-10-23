"""
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or head.next==None:
            return head
        n=n1=head
        while(n.next and n.next.next):
            n1=n1.next
            n=n.next.next
        l2=n1.next
        n1.next=None
        l1=head
        return self.merge(self.sortList(l1),self.sortList(l2))
        
    def merge(self,l1,l2):
        if not l2:
            return l1
        elif not l1:
            return l2
        else:
            head=start=ListNode(0)
            while(l1 and l2):
                if l1.val>l2.val:
                    head.next=l2
                    l2=l2.next
                else:
                    head.next=l1
                    l1=l1.next
                head=head.next
            if l1:
                head.next=l1
            else:
                head.next=l2
            return start.next
