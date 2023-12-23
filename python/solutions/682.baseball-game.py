#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start

# Solution: Stack
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
  def calPoints(self, operations: list[str]) -> int:
    score_stack = []

    for op in operations:
      if op == '+':
        score_stack.append(score_stack[-1] + score_stack[-2])
      elif op == 'D':
        score_stack.append(score_stack[-1] * 2)
      elif op == 'C':
        score_stack.pop()
      else:
        score_stack.append(int(op))

    return sum(score_stack)
# @lc code=end
