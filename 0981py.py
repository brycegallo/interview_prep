# leetcode 0981 - Time Based Key-Value Store

# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps
# and retrieve the key's value at a certain timestamp.
#
# Implement the TimeMap class:
#     TimeMap() Initializes the object of the data structure.
#     void set(String key, String value, int timestamp)
#           Stores the key key with the value value at the given time timestamp.
#     String get(String key, int timestamp)
#           Returns a value such that set was called previously, with timestamp_prev <= timestamp.
#           If there are multiple such values, it returns the value associated with the largest timestamp_prev.
#           If there are no values, it returns "".
class TimeMap:

    def __init__(self):
        self.store = {}  # key: list of [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""  # return empty string if there are no values
        values = self.store.get(key, [])

        # binary search operation
        left, right = 0, len(values) - 1
        while left <= right:
            middle = (left + right) // 2
            if values[middle][1] <= timestamp:
                result = values[middle][0]
                left = middle + 1
            else:
                right = middle - 1

        return result
