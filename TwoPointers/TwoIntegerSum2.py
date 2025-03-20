# Given an array of integers numbers that is sorted in non-decreasing order.

class Solution:
    def twoSum2(self,nums:list[int],target:int) -> list[int]:
        l, r = 0, len(nums) - 1

        while l<r:
            curSum = nums[l] + nums [r] #Calculate the Current Sum of Left & Right Pointers

            if curSum > target: #If curSum is greater than target, Decrement the Position of Right Pointer
                r -= 1
            elif curSum < target: #If curSum is less than target, Increment the Position of Left Pointer
                l += 1
            else:
                return [l+1,r+1] #Return the correct pointers which adds up to the sum of target

sol = Solution()
print(sol.twoSum2([1,2,3,5],8))
output = [3,4]
# Time : O(n), Space : O(1)