# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

class Solution:
    def longestConsecutive(self, nums: list[int]) -> bool:
        numSet = set(nums)  
        longest = 0

        for n in numSet: #Navigate through the Set
            if (n-1) not in numSet: #If (n-1) doesn't exist in Set then n is the start of sequence
                length = 0          #Initialize Length to 0
                while (n+length) in numSet: #Check if n+1 is in NumSet, then increment Length
                    length +=1
                longest = max(length,longest) #compute the Longest between Length and Longest
        
        return longest
        
sol = Solution()
nums = [2,20,4,10,3,4,5,6]
print(sol.longestConsecutive(nums))
# Time : O(n), Space : O(n)