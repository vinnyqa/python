# Design a data structure that supports adding new words and searching for existing words.
# Implement the WordDictionary class:
# void addWord(word) Adds word to the data structure.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

class WordDictionary:

    def __init__(self):
        self.store = [] #Have a Empty List

    def addWord(self, word: str) -> None:
        self.store.append(word) #Append Word

    def search(self, word: str) -> bool:
        for w in self.store: #For every word in Store List
            if len(w) != len(word): #If length is not same continue the loop
                continue
            i = 0
            while i < len(w):
                if w[i] == word[i] or word[i] == '.': #Match character by character or check if word[i] has a dot
                    i += 1
                else:
                    break
            if i == len(w): #If Counter i is equal to length of Word, return true
                return True
        return False

input = ["WordDictionary", "addWord", "bad", "addWord", "dad", "addWord", "mad", "search", "pad", "search", "bad", "search", ".ad", "search", "b.."]
output = [null,null,null,null,false,true,true,true]
# Time : O(1) for AddWord, O(m*n) for search(), Space : O(m*n)