# You are given an integer array heights where heights[i] represents the height of the ith bar.
# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l) #Area of Rectangle is Width * Length. Width is r-l. Length is the Min Length to avoid spill over.
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res

sol = Solution()
nums = [1,7,2,5,4,7,3,6]
print(sol.maxArea(nums))
output = 36
# Time : O(n), Space : O(1)