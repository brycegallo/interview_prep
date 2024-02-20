# leetcode 0912 - Sort an Array
# Medium - Arrays & Hashing
#
# Given an array of integers nums, sort the array in ascending order and return it.
#
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity
# and with the smallest space complexity possible.
# Time: O(n logn) Space: O(n)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, iStart, iMiddle, iEnd):
            leftHalf = arr[iStart: iMiddle + 1]
            rightHalf = arr[iMiddle + 1: iEnd + 1]

            iL = 0  # index for left half
            iR = 0  # index for right half
            iA = iStart  # index for arr

            # Merge the two sorted halfs into original array
            while iL < len(leftHalf) and iR < len(rightHalf):
                if leftHalf[iL] <= rightHalf[iR]:
                    arr[iA] = leftHalf[iL]
                    iL += 1
                else:
                    arr[iA] = rightHalf[iR]
                    iR += 1
                iA += 1

            # One half will have elements left over
            while iL < len(leftHalf):
                arr[iA] = leftHalf[iL]
                iL += 1
                iA += 1
            while iR < len(rightHalf):
                arr[iA] = rightHalf[iR]
                iR += 1
                iA += 1


        def mergeSort(arr, iStart, iEnd):
            # base case, array is a single element (technically sorted)
            if iEnd - iStart + 1 <= 1:
                return arr

            # get middle index of array
            iMiddle = (iStart + iEnd) // 2

            # sort left half
            mergeSort(arr, iStart, iMiddle)
            # sort right half
            mergeSort(arr, iMiddle + 1, iEnd)

            merge(arr, iStart, iMiddle, iEnd)

            return arr

        return mergeSort(nums, 0, len(nums) - 1)
