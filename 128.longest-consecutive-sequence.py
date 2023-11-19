#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start

# Solution #1: Use a set to hold all numbers then iterate over them looking to see which start sequences (no left neighbor)
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for n in nums_set:
            if n - 1 not in nums_set:
                length = 1

                while n + length in nums_set:
                    length += 1

                longest = max(longest, length)

        return longest


solution = Solution()
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))


# @lc code=end
