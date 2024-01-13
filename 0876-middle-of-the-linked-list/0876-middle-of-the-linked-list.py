# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        nodeCounter = 1
        
        pastNode = head
        curNode = head.next
        while True:
            if curNode:
                nodeCounter += 1
                pastNode = curNode
                curNode = pastNode.next
            else:
                break
        
        res = head
        for _ in range(nodeCounter//2):
            res = res.next
            
        return res