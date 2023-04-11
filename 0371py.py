# leetcode 0371 - Sum of Two Integers
# Given two integers a and b, return the sum of the two integers
# without using the operators + and -.
# Java Solution
# class Solution {
#     public int getSum(int a, int b) {
#         while (b != 0) {
#             int tmp = (a & b) << 1;
#             a = a ^ b;
#             b = tmp;
#         }
#         return a;
#     }
# }

# python solution using masking
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff

        while b != 0:
            temp = (a & b) << 1
            # ANDing with the mask keeps everything in 32 bits, because python can have unlimited leading 1s
            a = (a ^ b) & mask
            b = temp & mask

        # if a is greater than the mask, that means it is representing a negative number
        # we use
        if a > mask // 2:
            return ~(a ^ mask)
        return a
