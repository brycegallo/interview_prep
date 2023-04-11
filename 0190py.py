# leetcode 0190 - Reverse Bits

# Reverse bits of a given 32 bits unsigned integer.

# Note:
#
#     Note that in some languages, such as Java, there is no unsigned integer type.
#     In this case, the input will be given as a signed integer type.
#     It should not affect your implementation, as the integer's internal binary representation is the same,
#     whether it is signed or unsigned.
#     In Java, the compiler represents the signed integers using 2's complement notation.

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):
            bit = (n >> i) & 1
            result = result | (bit << (31-i))
        return result

class SimplifiedSolution:  # easier to visualize
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):
            result = result << 1
            bit = n % 2
            result += bit
            n = n >> 1

        return result
