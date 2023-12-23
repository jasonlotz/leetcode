#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
#

# Solution #1: Using dicts
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False

    s_dict = {}
    t_dict = {}
    for i in s:
      s_dict[i] = 1 + s_dict.get(i, 0)
    for i in t:
      t_dict[i] = 1 + t_dict.get(i, 0)

    return s_dict == t_dict

# Solution #2: Sorting first
# Time complexity: O(nlogn)
# Space complexity: O(1)
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)

# @lc code=end
