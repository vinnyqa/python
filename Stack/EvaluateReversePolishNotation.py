
# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
# Return the integer that represents the evaluation of the expression.
# The operands may be integers or the results of other operations.
# The operators include '+', '-', '*', and '/'.
# Assume that division between integers always truncates toward zero.

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop()) #Pop from Stack twice, Add & Append to Stack
            elif c == "*":
                stack.append(stack.pop() * stack.pop()) #Pop from Stack twice, Multiple & Append to Stack
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a) #Subtract 2nd one from 1st, Append to Stack
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a)) #Divide 2nd one from 1st, Append to Stack
            else:
                stack.append(int(c))
        return stack[0] #Return Single Value which is in Stack at stack[0]

sol = Solution()
tokens=["2","1","+","3","*"]
print(sol.evalRPN(tokens))
# Time : O(n), Space : O(n)