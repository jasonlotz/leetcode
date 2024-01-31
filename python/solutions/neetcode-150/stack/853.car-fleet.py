#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start

# Solution:
#   Sort by position then calculate time to target for each car and add to stack.
#   If time to target is less than previous car, then it is part of the same fleet.
#   If time to target is greater than previous car, then it is a new fleet.  Return the length of the stack.
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pair, reverse=True):
            stack.append((target - p) / s)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
# @lc code=end
