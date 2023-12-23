#
# @lc app=leetcode id=1496 lang=python3
#
# [1496] Path Crossing
#

# @lc code=start

# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
  def isPathCrossing(self, path: str) -> bool:
    visited = set()

    current_point = [0, 0]
    visited.add(tuple(current_point))

    for p in path:
      if p == 'N':
        current_point[1] += 1
      elif p == 'S':
        current_point[1] -= 1
      elif p == 'E':
        current_point[0] += 1
      elif p == 'W':
        current_point[0] -= 1

      if tuple(current_point) in visited:
        return True
      else:
        visited.add(tuple(current_point))

    return False

# @lc code=end
