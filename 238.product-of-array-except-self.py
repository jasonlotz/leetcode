#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start

# Solution #1: Two passes over array to compute prefix and then suffix products
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)

        # First pass, left to right to compute prefix products
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # Second pass, right to left to compute postfix products
        # and then multiply with prefix products
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
            print(result)

        return result


# @lc code=end
