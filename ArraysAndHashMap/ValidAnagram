# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 256 # Declare Array of 256 Characters for Lowercase/Uppercase/Special Characters ASCII Letters. 
        if len(s) != len(t): #97 = ASCII value a, 65 = ASCII value of A
            return False
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1 # Increment Array to traverse 1st String & Store diff from ASCII a. 
            count[ord(t[i]) - ord('a')] -= 1 # Decrement Array to traverse 2nd String & Store diff from ASCII a.

        for val in count:
            if val != 0:
                return False
        return True ## If Value is 0, perfect Anagram
        
sol = Solution()
s = "racecar"
t = "carrAce"
print(sol.isAnagram(s,t))
# Time : O(s+t), Space : O(1)