# leetcode 0338- Counting Bits
# Given an integer n, return an array ans of length n + 1 such that
# for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
class Solution1:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        offset = 1
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            ans[i] = 1 + ans[i-offset]
        return ans


# alternative solution, maybe more intuitive
class Solution2:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
