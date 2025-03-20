# Given the root of a binary tree, return its depth.
# The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Recursive Depth First Search (DFS)

class Solution:
    def maxDepth(self, root: [TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

sol = Solution()
root=[1,2,3,null,null,4]
output = 3
print(sol.maxDepth(root))
# Time : O(n), Space : O(n)
# ITERATIVE BINARY SEARCH