# leetcode 0146 - LRU Cache
# Medium
#
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#
# Implement the LRUCache class:
#
#     LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
#     int get(int key) Return the value of the key if the key exists, otherwise return -1.
#     void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
#
# The functions get and put must each run in O(1) average time complexity.
# Time: ? Memory: ?
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # maps keys to nodes

        # placeholder nodes. left shows LRU: least recently used, right shows most
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # remove from list
    def remove(self, node):
        prevnode = node.prev
        nextnode = node.next
        prevnode.next = nextnode
        nextnode.prev = prevnode

    # insert to the right
    def insert(self, node):
        prevnode = self.right.prev
        nextnode = self.right
        prevnode.next = nextnode.prev = node
        node.next, node.prev = nextnode, prevnode

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove LRU Node from list and delete LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
