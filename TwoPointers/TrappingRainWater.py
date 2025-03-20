# You are given an array non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.
# Return the maximum area of water that can be trapped between the bars.

class Solution:
    def trap(self, height: list[int]) -> int:
        if not height: 
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r] #leftMax & rightMax will initially set to height of respective index
        res = 0

        while l<r:
            if leftMax < rightMax: 
                l += 1
                leftMax = max(leftMax, height[l]) #Update leftMax with Maximum of leftMax and height of position Left
                res += leftMax - height[l] #Computed different of leftMax and height of position Left is added to Result Array
            else:
                r -= 1
                rightMax = max(rightMax, height[r]) #Update rightMax with Maximum of rightMax and height of position Right
                res += rightMax - height[r] #Computed different of rightMax and height of position Right is added to Result Array
        return res

sol = Solution()
height=[0,2,0,3,1,0,1,3,2,1]
output = 9
print(sol.trap(height))
# Time : O(n), Space : O(1)