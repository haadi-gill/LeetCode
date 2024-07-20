def go(node, arr):
    if (node != None):
        arr.append(node.val)
        go(node.left, arr)
        go(node.right, arr)



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        all = []
        go(root, all)
        all = sorted(all)
        print(all)

        root = TreeNode(all[0])
        currNode = root

        for a in all[1:]:
            currNode.right = TreeNode(a)
            currNode = currNode.right

        return root