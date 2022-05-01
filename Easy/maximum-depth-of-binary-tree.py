# from typing import *

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def getMaxDepth(node: TreeNode) -> int:
    if node is None:
        return 0
    return max(getMaxDepth(node.left), getMaxDepth(node.right)) + 1


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return getMaxDepth(root)
