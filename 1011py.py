# leetcode 1011 - Capacity To Ship Packages Within D Days
# Medium - Binary Search
#
# A conveyor belt has packages that must be shipped from one port to another within days days.
#
# The ith package on the conveyor belt has a weight of weights[i].
# Each day, we load the ship with packages on the conveyor belt (in the order given by weights).
# We may not load more weight than the maximum weight capacity of the ship.
#
# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped
# within days days.
# Time: O(m * logn) Memory: O(1)
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        result = high

        def canShip(capacity):
            ship_count, current_capacity = 1, capacity
            for weight in weights:
                if current_capacity - weight < 0:
                    ship_count += 1
                    current_capacity = capacity
                current_capacity -= weight
            return ship_count <= days

        while low <= high:
            middle_capacity = low + ((high - low) // 2)
            if canShip(middle_capacity):
                result = min(result, middle_capacity)
                high = middle_capacity - 1
            else:
                low = middle_capacity + 1

        return result
