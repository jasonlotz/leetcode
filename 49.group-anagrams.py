#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start

# Solution #1: Using an array of letters as keys in a hashmap of anagrams
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

# @lc code=end
