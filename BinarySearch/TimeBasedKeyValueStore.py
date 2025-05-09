# Implement a time-based key-value data structure that supports:
# Storing multiple values for the same key at specified time stamps
# Retrieving the key's value at a specified timestamp
# Implement the TimeMap class:
# TimeMap() Initializes the object.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns the most recent value of key if set was previously called on it and the most recent timestamp for that key prev_timestamp is less than or equal to the given timestamp (prev_timestamp <= timestamp). If there are no values, it returns "".
# Note: For all calls to set, the timestamps are in strictly increasing order.

class TimeMap:

    def __init__(self):
        self.store = {} # key: list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store: #Check if key exists in Store
            self.store[key] = [] #Insert key into Store and initialize Empty List
        self.store[key].append([value,timestamp]) #Append value and timestamp to the list

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, []) #Get the value based on key or by default empty list

        # binary search
        l, r =0, len(values) - 1
        while l<=r:
            m = (l+r) // 2 #In Python integer division uses 2 Slashes, single / does decimal division
            if values[m][1] <= timestamp: #values will contain pair of values. We only need 2nd value which is timestamp so use values[m][1]
                res = values[m][0] #Closed value we have seen before
                l = m + 1
            else:
                r = m - 1 #Invalid Value don't assign it to Result Array
        return res

sol = TimeMap(["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]])
# Time : O(1) for set and O(logn) for get, Space : O(m*n)