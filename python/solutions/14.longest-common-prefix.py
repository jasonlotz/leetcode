#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start

# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
  def longestCommonPrefix(self, strs: list[str]) -> str:
    prefix = None

    for str in strs:
      if prefix is None:
        prefix = str

      while not str.startswith(prefix):
        prefix = prefix[:-1]

    return prefix if prefix is not None else ""

# @lc code=end
