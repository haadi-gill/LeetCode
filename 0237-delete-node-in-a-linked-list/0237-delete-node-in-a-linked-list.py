# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        currNode = node
        while currNode != None:
            if currNode.next != None:
                currNode.val = currNode.next.val
                if currNode.next.next == None:
                    currNode.next = None
            else:
                currNode.val = None
            currNode = currNode.next
        
        