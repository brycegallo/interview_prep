# leetcode 0215 - Kth Largest Element in an Array
# Medium - Heap / Priority Queue
#
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# You must solve it in O(n) time complexity.
# Time: O(n^2 Worst Case, n Average Case) Memory: O(n)
class QuickSelectSolution:  # ideal for interviews
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k  # reassign k so that it points to k's eventual index

        def quickSelect(left, right):
            pivot, pointer = nums[right], left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[pointer], nums[i] = nums[i], nums[pointer]
                    pointer += 1
            nums[pointer], nums[right] = nums[right], nums[pointer]  # nums[right] here is the pivot

            if pointer > k:
                return quickSelect(left, pointer - 1)
            elif pointer < k:
                return quickSelect(pointer + 1, right)
            else:
                return nums[pointer]

        return quickSelect(0, len(nums) - 1)


class TrivialSolution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]


class SubOptimalSolution:  # Time: O(n + klogn) Memory: O(n)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negative_nums = [i * -1 for i in nums]
        heapq.heapify(negative_nums)
        while k:
            result = heapq.heappop(negative_nums)
            k -= 1
        return result * -1