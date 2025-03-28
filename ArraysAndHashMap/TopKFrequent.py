# Given an integer array nums and an integer k, return the k most frequent elements within the array.
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k:int) -> list[int]:
        count = {} 
        freq = [[] for n in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1+count.get(n,0) # Map the Frequency of Elements to Hashmap as Values.
        for n,c in count.items():
            freq[c].append(n) # Create a Frequency Array of Array freq[[]], Store Values in the place of Index
        res = [] # Create a Result Array res[], Append the Values and Stop when length of Array equals the Top K target
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

sol = Solution()
print(sol.topKFrequent([3,3,3,3,2,2],2))
# Time : O(n), Space : O(n) 
# Bucket Sort Approach