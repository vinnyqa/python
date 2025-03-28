# Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.
# Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.ary tree root, return the diameter of the tree.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Recursive Depth First Search (DFS)

class Solution:
    def isSameTree(self, p: Optional[TreeNode], subRoot: q[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

sol = Solution()
p=[1,2,3,4,5]
q=[2,4,5]
output = true
print(sol.isSameTree(p,q))
# Time : O(m*n), Space : O(m+n)