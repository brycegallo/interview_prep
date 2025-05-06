# leetcode 0347 - Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for _ in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            frequency[c].append(n)
        result = []
        for i in range(len(frequency) -1, 0, -1):
            for n in frequency[i]:
                result.append(n)
                if len(result) == k:
                    return result
