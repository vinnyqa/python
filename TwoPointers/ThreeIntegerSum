# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

class Solution:
    def threeSum(self,nums:list[int]) -> list[list[int]]:
        res = []
        nums.sort() #sort the Input Array

        for i,a in enumerate(nums):
            if (i>0 and a == nums[i-1]): #If this isn't the first value & same as previous value, then skip & continue the loop
                continue 

            l,r = i +1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r] #Calculate ThreeSum by adding the Current Value and Left,Right Pointer Value
                if(threeSum>0): #If threeSum>0 Decrement the Right Pointer
                    r -= 1
                elif(threeSum<0): #If threeSum<0 Increment the Left Pointer
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]]) #Append the Current Value, Left, Right Pointer Value to Result Array
                    l += 1 #Increment the Left Pointer
                    while nums[l] == nums[l - 1] and l < r: #If current value is duplicate of previous value, then increment left pointer
                        l += 1 
        return res

sol = Solution()
nums1 = [-1,0,1,2,-1,-4]
nums2 = [0,1,1]
print(sol.threeSum(nums1))
print(sol.threeSum(nums2))

# Time : O(n2), Space : O(1) or o(n)