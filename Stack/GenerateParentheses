
# You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.
# BACKTRACKING SOLUTION
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n: #Valid if Open is equal to Closing Parenthesis count
                res.append("".join(stack))
                return

            if openN < n: #add Open Parenthesis if Open < n
                stack.append("(") 
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN: #add Closing Parenthesis if Closed < Open
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()

        backtrack(0,0)
        return res

sol = Solution()
n= 5
print(sol.generateParenthesis(n))
# Time : O(4^n/square root of n), Space : O(n)
#Backtracking Solution 3 Open, 3 Close, close < open