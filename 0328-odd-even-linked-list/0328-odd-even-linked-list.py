# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: 
            return None
        if head.next is None: 
            return head
        
        o = head
        p = o.next
        ehead = p
        while p.next is not None:
            o.next = p.next
            p.next = p.next.next
            o = o.next
            p = p.next
            
            if p is None: 
                break
                
        o.next = ehead
        return head