# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i]   = prefix    # 1 1 2 6
            prefix  *= nums[i]   # 1 2 6 24

        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i]   *= postfix  #[1, 1, 2, 6] [1, 1, 8, 6] [1, 12, 8, 6] [24, 12, 8, 6]
            postfix  *= nums[i]  # 4 12 24 24
        return res
    
sol = Solution()
nums=[1,2,3,4]
sol.productExceptSelf(nums)
# Time : O(n), Space : O(1) since the output array is excluded from space analysis.
# Set the Prefix to 1,Multiply the Prefix before visiting the next pos in Array & replace the value in Output Array
# Set the Postfix to 1,Multiply the Postfix with Output Array value & also Multiply the Postfix with nums Array before visiting the next pos in Array & replace the value in Output Array