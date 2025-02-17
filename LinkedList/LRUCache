# Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations
# LRUCache(int capacity) Initialize the LRU cache of size capacity.
# int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
# `OrderedDict` maintains the sequence in which keys are added, ensuring that the order is preserved during iteration
# BUILT-IN DATA STRUCTURE

from typing import OrderedDict

class LRUCache:

    def __init__(self, capacity: int): 
        self.cache = OrderedDict() #Initialize the Cache as Ordered Dictionary to maintain the Order of Dictionary 
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key) ## Move the key to  end
        return self.cache[key] #Return the Value associated with Get Key

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value #Assign the Value passed in Put function to corresponding key

        if len(self.cache) > self.cap:
            self.cache.popitem(last=False) #If the last is False then this method would delete a key from the beginning of the dictionary. 
            #This serves as FIFO(First In First Out) in the queue otherwise it method would delete the key from the end of the dictionary.

input=["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]
output = [null,null,10,null,null,20,-1]
# Time : O(1) for each put() and get(), Space : O(n)