# Given a string s, return true if it is a palindrome, otherwise return false.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1 #Left pointer at 0, Right at Length of S -1

        while l < r:
            while l < r and not self.alphaNum(s[l]): #Verify the character is not Alphanumeric. If it is increment the Left pointer
                l += 1
            while r > l and not self.alphaNum(s[r]): #Verify the character is not Alphanumeric. If it is decrement the Right pointer
                r -= 1

            if s[l].lower() != s[r].lower(): #Convert characters to Lowercase & Compare Left and Right. If they are not equal return False
                return False
            
            l, r = l + 1, r - 1 #Increment the Left & Decrement the Right Pointer
        return True

    def alphaNum(self, c): #Helper Function to determine the character is Alpha Numeric or not
           return (ord('A') <= ord(c) <= ord('Z') or 
                    ord('a') <= ord(c) <= ord('z') or 
                    ord('0') <= ord(c) <= ord('9'))

sol = Solution()
print(sol.isPalindrome("Was it a car or a cat I saw?"))
# Time : O(n), Space : O(1)