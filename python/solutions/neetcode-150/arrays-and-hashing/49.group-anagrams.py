#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start

# Solution #1:
#   For each word, create a tuple of 26 elements where each element is the count of the character in the word.
#   Store the tuple as key in a dictionary and append the word to the list of values for the key.
#   Return the values of the dictionary.
#
# Time complexity: O(m * n) [m = average string length, n = number of strings]
# Space complexity: O(n)
from collections import defaultdict


class Solution:
  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    result = defaultdict(list)

    for s in strs:
      count = [0] * 26

      for c in s:
        count[ord(c) - ord('a')] += 1

      result[tuple(count)].append(s)
    return result.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))

# @lc code=end
