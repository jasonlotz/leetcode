#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start

# Solution: Two-pointers (one at each end) moving whichever is shorter
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
  def maxArea(self, height: list[int]) -> int:
    max_area = 0

    left_index = 0
    right_index = len(height) - 1

    while left_index < right_index:
      area = (min(height[left_index], height[right_index])
              * (right_index - left_index))

      if height[left_index] < height[right_index]:
        left_index += 1
      else:
        right_index -= 1

      max_area = max(max_area, area)
    return max_area


assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert Solution().maxArea([1, 1]) == 1
# @lc code=end
