#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start

# Solution: Two pointers
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        left = 0
        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]

        return left+1

# @lc code=end
