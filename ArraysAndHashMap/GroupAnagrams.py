# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list) # mapping charCount to List of Anagrams

        for s in strs:
            count = [0]*26 # Array of size O(26), since character set is a through z (26 continuous characters), to count the frequency of each character in a string.
            ## Use this array as the key in the hash map to group the strings.
             
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s) #List cant become a Key in Python

        return res.values()
    
sol = Solution()
strs = ["act","cat","vineetha"]
print(sol.groupAnagrams(strs))
             
# Time : O(m*n), Space : O(m) where m is the num of strings and n is the length of the longest String
# User gets TypeError: unhashable type: 'list' when we try to append List as Key to res[] without converting to tuple. Example: res[count].append(s)