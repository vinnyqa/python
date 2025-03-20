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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

sol = Solution()
root=[4,2,7,1,3,6,9]
output = [4,7,2,9,6,3,1]
print(sol.invertTree(root))
# Time : O(n), Space : O(n)
# ITERATIVE BINARY SEARCH