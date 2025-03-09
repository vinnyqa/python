# The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.
# The length of a path between two nodes in a binary tree is the number of edges between the nodes.
# Given the root of a binary tree root, return the diameter of the tree.
# DEPTH FIRST SEARCH

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return res

sol = Solution()
root=[1,null,2,3,4,5]
output = 3
print(sol.diameterOfBinaryTree(root))
# Time : O(n), Space : O(n)