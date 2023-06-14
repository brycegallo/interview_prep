# leetcode 0735 - Asteroid Collision
# Medium - Stack
#
# We are given an array asteroids of integers representing asteroids in a row.
#
# For each asteroid, the absolute value represents its size, and the sign represents its direction
# (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
#
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode.
# If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
# Time: O(n) Memory: O(n)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                difference = asteroid + stack[-1]
                if difference < 0:
                    stack.pop()
                elif difference > 0:
                    asteroid = 0
                else:
                    stack.pop()
                    asteroid = 0
            if asteroid:
                stack.append(asteroid)

        return stack
