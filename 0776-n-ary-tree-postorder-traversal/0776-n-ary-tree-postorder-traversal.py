"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
def helper(root, output):
    for c in root.children:
        helper(c, output)
    output.append(root.val)

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        output = []

        if root == None:
            return []

        helper(root, output)

        return output
        