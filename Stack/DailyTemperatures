# You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.
# Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = [] # pair: [index,height]

        for i,t in enumerate(temperatures): # i=index, t= temp
            while stack and t > stack[-1][0]: #While Stack is empty & Temp is greater than Top of Stack (stack[-1]) & First Value of Stack (stack[0])
                stackT, stackIndex = stack.pop()
                res[stackIndex] = (i-stackIndex) #Compute Number of Days it takes for Day with Warmer Temp = i-stackIndex (Current Index - Stack Index)
            stack.append([t,i])
        return res

sol = Solution()
print(sol.dailyTemperatures([1,2,3,5,8]))

# Time : O(n), Space : O(n)