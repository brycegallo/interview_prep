# Implementation of a Hash-Table in Python
class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * self.capacity

    def hash_function(self, key):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        node = self.table[index]

        if not node:
            self.table[index] = Node(key, value)
        else:
            previous = None
            while node:
                if node.key == key:
                    node.value = value
                    return
                previous, node = node, node.next
            previous.next = Node(key, value)
        self.size += 1
        
        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash_function(key)
        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        node = self.table[index]
        previous = None

        while node:
            if node.key == key:
                if previous:
                    previous.next = node.next
                else:
                    self.table[index] = node.next
                self.size -= 1
                return True
                
            previous, node = node, node.next

        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        new_table = [None] * self.capacity

        for node in self.table:
            while node:
                index = node.key % self.capacity
                if new_table[index] == None:
                    new_table[index] = Node(node.key, node.value)
                else:
                    new_node = new_table[index]
                    node.next = new_node
                    new_table[index] = node
                node = node.next

        self.table = new_table
