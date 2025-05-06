# leetcode 0303 - Range Sum Query - Immutable
# Easy - Arrays & Hashing
#
# Given an integer array nums, handle multiple queries of the following type:
#
#     Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
#
# Implement the NumArray class:
#
#     NumArray(int[] nums) Initializes the object with the integer array nums.
#     int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive
#     (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# Naive Approach
# Time: O(n) Space: O(1)
class NumArrayNaive:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for i in range(left, right + 1):
            sum += self.nums[i]
        return sum


# Precalculation Approach
# Time: setup O(n), successive calls O(1) Space: O(n)
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_array = []
        current_sum = 0
        for num in nums:
            current_sum += num
            self.prefix_array.append(current_sum)

    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.prefix_array[right]
        left_sum = self.prefix_array[left - 1] if left > 0 else 0
        return right_sum - left_sum