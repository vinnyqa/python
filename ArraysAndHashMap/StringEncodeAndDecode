# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s #Derive Encoded Result String which is having Delimiter #, Length of String and Whole string
        return res
    
    def decode(self, s:str) -> list[str]:
        res = []
        i = 0
        while (i<len(s)):
            j=i #Have a j pointer initialized to i at the start
            while s[j] != "#": #Increment j until its not equal to delimiter #
                j += 1
            length = int(s[i:j]) #Length of String is starting from Index i until j not including j
            i = j + 1 #Increment i to j+1 as j is at Delimiter
            j = i + length #Increment j to i+length to grab whole string
            res.append(s[i:j]) #Append whole string to Result Array from i to j excluding j
            i = j #Assign j to i to continue loop further
        return res

# Time : O(m), Space : O(1) where m is the sum of lengths of all strings and n is num of strings.
sol = Solution()
input = ["neet","code","love","you"]
encoded = sol.encode(input)
print(encoded)
#4#neet4#code4#love3#you
print(sol.decode(encoded))
["neet","code","love","you"]