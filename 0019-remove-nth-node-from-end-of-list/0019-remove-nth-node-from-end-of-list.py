# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)  # 더미 노드 생성 (head가 삭제될 수도 있으므로)
        dummy.next = head
        fast = slow = dummy  # 두 포인터 초기화

        # Step 1: fast를 n칸 앞으로 이동
        for _ in range(n + 1):  # +1 하는 이유는 slow가 삭제할 노드의 이전 노드에 위치하도록 하기 위함
            fast = fast.next
        
        # Step 2: fast가 끝까지 갈 때까지 slow와 함께 이동
        while fast:
            fast = fast.next
            slow = slow.next
        
        # Step 3: slow.next를 삭제
        slow.next = slow.next.next

        return dummy.next  # 더미 노드의 next가 새로운 head