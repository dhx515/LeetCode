class Solution(object):
    def removeElements(self, head, val):
        temp = head

        while temp and temp.val == val:
            temp = temp.next
        
        ret = temp
        prev = temp

        while temp:
            if temp.val != val:
                if temp != prev:
                    prev.next = temp
                prev = temp
            temp = temp.next
        if prev:
            prev.next = None
        return ret