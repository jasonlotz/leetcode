#
# @lc app=leetcode id=1422 lang=python3
#
# [1422] Maximum Score After Splitting a String
#

# @lc code=start

# Solution 1: 2 passes (first to count 1s, second to calculate max score)
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
  def maxScore(self, s: str) -> int:
    ones = s.count("1")
    zeros = 0
    result = 0

    for i in range(len(s) - 1):
      if s[i] == "1":
        ones -= 1
      else:
        zeros += 1

      result = max(result, zeros + ones)

    return result


assert (Solution().maxScore("011101") == 5)
assert (Solution().maxScore("1111") == 3)
# @lc code=end
