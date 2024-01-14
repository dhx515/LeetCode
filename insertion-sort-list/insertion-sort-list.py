class Solution(object):
    def insertionSortList(self, head):

        cur = parent = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next
	    cur = parent
        
        return parent.next