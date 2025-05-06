# leetcode 1137 - N-th Tribonacci Number
# Easy - 1-D Dynamic Programming
#
# The Tribonacci sequence Tn is defined as follows:
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
#
# Given n, return the value of Tn.
# Time: O(n) Memory: O(1)
class MyFirstSolution:
    def tribonacci(self, n: int) -> int:
        result = 0
        arr = [0, 1, 1]

        if n < 3:
            return arr[n]
        while n - 2:
            result = sum(arr)
            arr[0], arr[1], arr[2] = arr[1], arr[2], result
            n -= 1

        return result


class SlightlyBetterSolution:
    def tribonacci(self, n: int) -> int:
        arr = [0, 1, 1]

        if n < 3:
            return arr[n]
        for i in range(3, n + 1):
            arr[0], arr[1], arr[2] = arr[1], arr[2], sum(arr)

        return arr[2]
