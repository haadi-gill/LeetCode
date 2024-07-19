# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1 = head
        p2 = head

        while p2.next != None:
            p2 = p2.next
            if p2.next == None:
                return p1.next
            p2 = p2.next
            p1 = p1.next
        return p1
        