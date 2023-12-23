#
# @lc app=leetcode id=1929 lang=python3
#
# [1929] Concatenation of Array
#

# @lc code=start

# Solution: Loop and append
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
  def getConcatenation(self, nums: list[int]) -> list[int]:
    for i in range(len(nums)):
      nums.append(nums[i])

    return nums
# @lc code=end
