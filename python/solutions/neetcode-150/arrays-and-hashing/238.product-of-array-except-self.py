#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start

# Solution #1: Two passes over array to compute prefix and then suffix products
# Time complexity: O(n)
# Space complexity: O(n)
# class Solution:
#   def productExceptSelf(self, nums: list[int]) -> list[int]:
#     result = [1] * len(nums)

#     # First pass, left to right to compute prefix products
#     prefix = 1
#     for i in range(len(nums)):
#       result[i] = prefix
#       prefix *= nums[i]

#     print(result)

#     # Second pass, right to left to compute postfix products
#     # and then multiply with prefix products
#     postfix = 1
#     for i in range(len(nums) - 1, -1, -1):
#       result[i] *= postfix
#       postfix *= nums[i]
#     print(result)

#     return result

# Solution #2: Two passes but slightly easier to understand approach
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        result = [0] * length

        # First pass, left to right to compute products of all elements to the left
        result[0] = 1
        for i in range(1, length):
            result[i] = nums[i - 1] * result[i - 1]

        # Second pass, right to left to compute the result products while tracking the products of all elements to the right
        products_to_right = 1
        for i in reversed(range(length)):
            result[i] = result[i] * products_to_right
            products_to_right *= nums[i]

        return result


assert (Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6])
# @lc code=end
