#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
# Solution: Binary search
# Time complexity: O(logn)
# Space complexity: O(1)
class Solution:
    def findMin(self, nums: list[int]) -> int:
        result = nums[0]

        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break

            mid = (left + right) // 2
            result = min(result, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return result

# @lc code=end
