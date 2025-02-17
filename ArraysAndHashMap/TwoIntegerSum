# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

class TwoIntegerSum:
    def twoSum(self,nums:list[int],target:int) -> list[int]:
        prevMap = {} #val ->index
        for i, n in enumerate(nums):
            diff = target-n # Traverse through the List, Calculate difference
            if diff in prevMap:
                return [prevMap[diff],i] # If difference is already in Hashmap return index of difference and current element index
            prevMap[n] = i # Else store the current element in the hashmap with its index and continue

sol = TwoIntegerSum()
print(sol.twoSum([1,2,3,5],7))

# Time : O(n), Space : O(n)
