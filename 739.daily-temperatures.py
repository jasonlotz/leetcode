#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start

# Solution: Using a stack to track the lower temperature which will be in monotonic decreasing order
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        temp_stack = []  # tuples: (temperature, index)

        for i, temp in enumerate(temperatures):
            while temp_stack and temp > temp_stack[-1][0]:
                _, temp_idx = temp_stack.pop()
                result[temp_idx] = i - temp_idx
            temp_stack.append((temp, i))

        return result


# @lc code=end
