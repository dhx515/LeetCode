# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        prev = None
        current = slow
        while current:
            next_node = current.next  # 다음 노드 저장
            current.next = prev       # 포인터 반전
            prev = current            # prev를 현재 노드로 이동
            current = next_node       # current를 다음 노드로 이동

        left = head
        right = prev  # 반전된 리스트의 시작점

        is_palindrome = True
        while right:
            if left.val != right.val:
                is_palindrome = False
                break
            left = left.next
            right = right.next

        return is_palindrome