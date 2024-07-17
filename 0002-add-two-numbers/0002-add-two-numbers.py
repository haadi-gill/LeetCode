# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # num1 = 0
        # currNode = l1
        # multiplier = 1
        # while currNode != None:
        #     num1 += (multiplier*currNode.val)
        #     multiplier *= 10
        #     currNode = currNode.next

        # num2 = 0
        # currNode = l2
        # multiplier = 1
        # while currNode != None:
        #     num1 += (multiplier*currNode.val)
        #     multiplier *= 10
        #     currNode = currNode.next

        # s = num1 + num2

        # sourceNode = ListNode()
        # currNode = sourceNode
        # while s > 0:
        #     currNode.val = s%10
        #     s = int(s/10)
        #     if s > 0:
        #         currNode.next = ListNode()
        #         currNode = currNode.next

        sourceNode = ListNode()
        currSource = sourceNode
        carry = 0

        while(l1 != None and l2 != None):
            s = carry + l1.val + l2.val
            carry = int(s/10)
            currSource.next = ListNode(s%10)
            l1 = l1.next
            l2 = l2.next
            currSource = currSource.next

        while(l1 != None):
            s = carry + l1.val
            carry = int(s/10)
            currSource.next = ListNode(s%10)
            l1 = l1.next
            currSource = currSource.next
            

        while(l2 != None):
            s = carry + l2.val
            carry = int(s/10)
            currSource.next = ListNode(s%10)
            l2 = l2.next
            currSource = currSource.next

        if carry:
            currSource.next = ListNode(carry)
            
        return sourceNode.next
