# You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.
# Return the area of the largest rectangle that can be formed among the bars.

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = [] # pair: [index,height]

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] >h: #While stack is non empty, Top value in Stack & Top Value's Height is greater than Height we reached
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i-index)) #Width = Current Index i - index
                start = index #This height is greater than current height we are visiting, extend the start index backwards to index we popped 
            stack.append((start, h)) #Add start index which we pushed to backwards and height we are visiting right now

        for i,h in stack: #There may be still some entries left in Histogram. Extend it to the end.
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea

sol = Solution()
heights = [1,3,7]
print(sol.largestRectangleArea(heights))

# Time : O(n), Space : O(n)