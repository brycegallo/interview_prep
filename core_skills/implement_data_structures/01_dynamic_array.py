# Implementation of a Dynamic Array (Resizable Array) in Python
class DynamicArray:
    
    # __init() T: O(n)
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.array = [0] * self.capacity

    # get() T: O(1)
    def get(self, i: int) -> int:
        return self.array[i]

    # set() T: O(1)
    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    # pushback() T: O(1) Ammortized
    # T: O(n) worst case, but rarely encountered
    def pushback(self, n: int) -> None:
        # check if array is already full, resize of necessary
        if self.length == self.capacity:
            self.resize()
        # insert at next empty position
        self.array[self.length] = n
        self.length += 1

    # popback() T: O(1)
    def popback(self) -> int:
        # check if array has anything to pop
        if self.length > 0:
            # soft deletion of last element
            self.length -= 1
        return self.array[self.length]

    # resize() T: O(n)
    def resize(self) -> None:
        # create new array with double capacity
        self.capacity = 2 * self.capacity
        new_array = [0] * self.capacity

        # copy elements to new array
        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array

    # getSize() T: O(1)
    def getSize(self) -> int:
        return self.length
    
    # getCapacity() T: O(1)
    def getCapacity(self) -> int:
        return self.capacity

