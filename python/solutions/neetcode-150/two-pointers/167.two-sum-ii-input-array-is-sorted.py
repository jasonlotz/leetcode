#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start

# Solution: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
  def twoSum(self, numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1

    while left < right:
      if numbers[left] + numbers[right] == target:
        return [left + 1, right + 1]
      elif numbers[left] + numbers[right] < target:
        left += 1
      else:
        right -= 1

# @lc code=end
