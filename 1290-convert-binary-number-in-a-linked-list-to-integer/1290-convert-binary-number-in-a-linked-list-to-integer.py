# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        ans = ""
        node = head
        while node:
            ans += str(node.val)
            node = node.next
        
        res = 0
        unit = 1
        for c in ans[::-1]:
            res += int(c)*unit
            unit *=2
        return res