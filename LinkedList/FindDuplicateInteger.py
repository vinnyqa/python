# You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.
# Every integer appears exactly once, except for one integer which appears two or more times. Return the integer that appears more than once.
# FLOYD'S ALGORITHM(SLOW AND FAST)

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = 0, 0 
        while True:
            slow = nums[slow] 
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

nums = [1,2,3,2,2]
output = 2
sol= Solution()
print(sol.findDuplicate(nums))
# Time : O(n), Space : O(1)