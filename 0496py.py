# leetcode 0496 - Next Greater Element I
# Easy - Arrays & Hashing
#
# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
#
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
#
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
#
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
# Time: O(m+n) Memory: O(m)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Index = {n: i for i, n in enumerate(nums1)}  # hashmap comprehension
        result = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            current = nums2[i]
            while stack and current > stack[-1]:
                value = stack.pop()
                index = nums1Index[value]
                result[index] = current
            if current in nums1Index:
                stack.append(current)

        return result

# less efficiient solution, O(n^2)
class BruteForceSolution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Index = {n: i for i, n in enumerate(nums1)}  # hashmap comprehension
        result = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in nums1Index:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    index = nums1Index[nums2[i]]
                    result[index] = nums2[j]
                    break
        return result
