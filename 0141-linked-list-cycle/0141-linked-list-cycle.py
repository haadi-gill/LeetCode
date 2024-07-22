# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        x = set()

        curr = head

        while(curr != None):
            if curr in x:
                return True
            x.add(curr)
            curr = curr.next
        return False
