# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False
        
sol = Solution()
nums = [1,2,3]
print(sol.hasDuplicate(nums))

# Time : O(n), Space : O(n)
# Loop thru the list. Add numbers to Hashset. If it already exists,return True. Duplicate Found. 
