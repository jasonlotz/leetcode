#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start

# Solution #1: Use a set
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)

        return False

# Solution #2: Sorting first
# Time complexity: O(nlogn)
# Space complexity: O(1)
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()

#         for i in range(len(nums) - 1):
#             if nums[i] == nums[i + 1]:
#                 return True

#         return False

# @lc code=end
