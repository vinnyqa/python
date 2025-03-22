# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
# The input string s is valid if and only if:
# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" } #Hashmap to map Open<->Close Parentheses

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]: #Stack is not empty and Value at the top of Stack(stack[-1]) matches with Hashmap Closing Parenthesis Value 
                    stack.pop() #Pop the Stack
                else:
                    return False #Stack is empty
            else:
                stack.append(c) #If we get Open Parenthesis we add it to Stack and Continue

        return True if not stack else False #Return True if Stack is Empty

sol = Solution()
s = "([{}])"
print(sol.isValid(s))
# Time : O(n), Space : O(n)