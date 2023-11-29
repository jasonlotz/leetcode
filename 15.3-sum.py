#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start

# Solution: Sort first, then use two pointers to find the combinations
# Time complexity: O(n^2)
# Space complexity: O(1)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        for i, num in enumerate(nums):

            # Skip the same number
            if i > 0 and num == nums[i - 1]:
                continue

            # Use two pointers to find the combinations
            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = num + nums[left] + nums[right]

                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    result.append([num, nums[left], nums[right]])

                    left += 1

                    # Skip the same number
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return result

# @lc code=end
