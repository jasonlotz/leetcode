#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start

# Solution #1: Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# Solution #2: Use a dict of complement: index
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        complement_dict = {}

        for i, value in enumerate(nums):
            complement = target - value

            if complement in complement_dict:
                return [complement_dict[complement], i]

            complement_dict[value] = i

# @lc code=end
