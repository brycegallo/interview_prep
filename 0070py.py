# leetcode 0070 - Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# NOT DP - Brute Force Recursive - exceeds leetcode time limit
class BruteRecursiveSolution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

# Iterative Solution
class MySolution:
    def climbStairs(self, n: int) -> int:
        temp, one, two = 0, 0, 1
        while n > 0:
            temp = one + two
            one, two = two, temp
            n -= 1
        return two

# Iterative Solution
class NeetCodeSolution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one
