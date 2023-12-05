#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start

# Solution: Two pointers
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        left = 0
        for right in range(0, len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1

        return left


sol = Solution()
result = sol.removeElement([3, 2, 2, 3], 3)
print(result)

# @lc code=end
