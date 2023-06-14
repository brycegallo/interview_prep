# leetcode 0605 - Can Place Flowers
# Easy - Arrays & Hashing
#
# You have a long flowerbed in which some of the plots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.
#
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
# return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule
# and false otherwise.
# Time: O(n) Memory: O(n)
class LinearMemorySolution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        flower_array = [0] + flowerbed + [0]
        for i in range(1, len(flower_array) - 1):
            if not (flower_array[i - 1] and flower_array[i] and flower_array[i + 1]):
                flower_array[i] = 1
                n -= 1
        return n <= 0


# Solution with O(1) space complexity
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empty = 0 if flowerbed[0] else 1

        for f in flowerbed:
           if f:
               n -= int((empty - 1) / 2)  # int division, round toward zero
               empty = 0
           else:
               empty += 1

        n -= (empty) // 2
        return n <= 0
